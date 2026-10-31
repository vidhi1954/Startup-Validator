import { FormEvent, useMemo, useState } from 'react';
import { submitIdea } from './api';
import type { AnalysisResult } from './types';

type Screen = 'login' | 'input' | 'output';

const defaultResult: AnalysisResult = {
  marketScore: 7.5,
  revenueScore: 6.8,
  overallScore: 7.1,
  recommendation: 'Validate demand with a small pilot before scaling.',
  swot: [
    'Strengths: clear user problem, targeted audience, AI-driven differentiation.',
    'Weaknesses: acquisition cost may be high and user conversion can be slow.',
    'Opportunities: strong growth in digital learning and AI tools.',
    'Threats: competition from established edtech platforms and low switching cost.',
  ],
  evidence: [
    'Industry trend report: AI-powered learning tools are growing quickly.',
    'Competitor comparison: subscription pricing is becoming the default model.',
    'Target audience insight: students are increasingly adopting digital tutors.',
  ],
};

function App() {
  const [screen, setScreen] = useState<Screen>('login');
  const [idea, setIdea] = useState('AI tutor for competitive programming');
  const [industry, setIndustry] = useState('EdTech');
  const [targetMarket, setTargetMarket] = useState('Indian college students');
  const [budget, setBudget] = useState(50000);
  const [businessModel, setBusinessModel] = useState('Subscription');
  const [result, setResult] = useState<AnalysisResult>(defaultResult);

  const isInputValid = useMemo(() => {
    return idea.trim().length > 0 && industry.trim().length > 0 && targetMarket.trim().length > 0;
  }, [idea, industry, targetMarket]);

  const handleLogin = (e: FormEvent) => {
    e.preventDefault();
    setScreen('input');
  };

  const handleAnalyze = async (e: FormEvent) => {
    e.preventDefault();

    if (!isInputValid) return;

    try {
      const response = await submitIdea({ idea });

      const marketAnalysis = response?.market_analysis ?? {};
      const revenueAnalysis = response?.revenue_analysis ?? {};
      const swotAnalysis = response?.swot_analysis ?? {};
      const startupScore = response?.startup_score ?? {};

      const nextResult: AnalysisResult = {
        marketScore: Number(startupScore.market_score ?? 0),
        revenueScore: Number(startupScore.revenue_score ?? 0),
        overallScore: Number(startupScore.overall_score ?? 0),
        recommendation: String(startupScore.recommendation ?? 'More validation needed before scaling.'),
        swot: [
          `Strengths: ${(swotAnalysis.strengths ?? []).join(', ') || 'Not available'}`,
          `Weaknesses: ${(swotAnalysis.weaknesses ?? []).join(', ') || 'Not available'}`,
          `Opportunities: ${(swotAnalysis.opportunities ?? []).join(', ') || 'Not available'}`,
          `Threats: ${(swotAnalysis.threats ?? []).join(', ') || 'Not available'}`,
        ],
        evidence: [
          `Target audience: ${marketAnalysis.target_audience || 'Not available'}`,
          `Market demand: ${marketAnalysis.market_demand || 'Not available'}`,
          `Challenges: ${(marketAnalysis.challenges ?? []).join(', ') || 'Not available'}`,
          `Pricing model: ${revenueAnalysis.pricing_model || 'Not available'}`,
          `Revenue streams: ${(revenueAnalysis.revenue_streams ?? []).join(', ') || 'Not available'}`,
        ],
      };

      setResult(nextResult);
      setScreen('output');
    } catch (error) {
      console.error('Analysis failed:', error);
      setResult({
        ...defaultResult,
        recommendation: `"${idea}" could not be analyzed right now. Please check the backend and try again.`,
      });
      setScreen('output');
    }
  };

  return (
    <div className="app-shell">
      <header className="topbar">
        <div className="brand">
          <span className="brand-mark">S</span>
          <span>Startup Validator</span>
        </div>
      </header>

      {screen === 'login' && (
        <main className="screen active">
          <section className="card auth-card">
            <div className="card-header">
              <p className="eyebrow">Welcome back</p>
              <h1>Login</h1>
            </div>

            <form className="form" onSubmit={handleLogin}>
              <label>
                <span>Email</span>
                <input type="email" placeholder="you@example.com" required />
              </label>

              <label>
                <span>Password</span>
                <input type="password" placeholder="••••••••" required />
              </label>

              <button type="submit" className="primary-btn">Login</button>
            </form>
          </section>
        </main>
      )}

      {screen === 'input' && (
        <main className="screen active">
          <section className="card form-card">
            <div className="card-header">
              <p className="eyebrow">Validate your idea</p>
              <h2>Startup input</h2>
            </div>

            <form className="form" onSubmit={handleAnalyze}>
              <label>
                <span>Startup idea</span>
                <textarea rows={4} value={idea} onChange={(e) => setIdea(e.target.value)} required />
              </label>

              <div className="two-col">
                <label>
                  <span>Industry</span>
                  <input type="text" value={industry} onChange={(e) => setIndustry(e.target.value)} required />
                </label>

                <label>
                  <span>Target market</span>
                  <input type="text" value={targetMarket} onChange={(e) => setTargetMarket(e.target.value)} required />
                </label>
              </div>

              <div className="two-col">
                <label>
                  <span>Budget</span>
                  <input type="number" value={budget} onChange={(e) => setBudget(Number(e.target.value))} required />
                </label>

                <label>
                  <span>Business model</span>
                  <select value={businessModel} onChange={(e) => setBusinessModel(e.target.value)}>
                    <option>Subscription</option>
                    <option>Freemium</option>
                    <option>B2B SaaS</option>
                    <option>Marketplace</option>
                  </select>
                </label>
              </div>

              <button type="submit" className="primary-btn" disabled={!isInputValid}>
                Analyze idea
              </button>
            </form>
          </section>
        </main>
      )}

      {screen === 'output' && (
        <main className="screen active">
          <section className="card results-card">
            <div className="card-header split-header">
              <div>
                <p className="eyebrow">Analysis result</p>
                <h2>Startup validation report</h2>
              </div>
              <button className="secondary-btn" onClick={() => setScreen('input')}>
                New analysis
              </button>
            </div>

            <div className="score-grid">
              <div className="score-box">
                <p>Market score</p>
                <h3>{result.marketScore.toFixed(1)}</h3>
              </div>
              <div className="score-box">
                <p>Revenue score</p>
                <h3>{result.revenueScore.toFixed(1)}</h3>
              </div>
              <div className="score-box highlight">
                <p>Overall score</p>
                <h3>{result.overallScore.toFixed(1)}</h3>
              </div>
            </div>

            <div className="report-section">
              <h3>Recommendation</h3>
              <p>{result.recommendation}</p>
            </div>

            <div className="report-grid">
              <div className="report-section">
                <h3>SWOT</h3>
                <ul>
                  {result.swot.map((item, index) => (
                    <li key={index}>{item}</li>
                  ))}
                </ul>
              </div>

              <div className="report-section">
                <h3>Evidence</h3>
                <ul>
                  {result.evidence.map((item, index) => (
                    <li key={index}>{item}</li>
                  ))}
                </ul>
              </div>
            </div>
          </section>
        </main>
      )}
    </div>
  );
}

export default App;
