export type Screen = 'login' | 'input' | 'output';

export type AnalysisResult = {
  marketScore: number;
  revenueScore: number;
  overallScore: number;
  recommendation: string;
  swot: string[];
  evidence: string[];
};

export type LoginPayload = {
  email: string;
  password: string;
};

export type StartupIdeaPayload = {
  idea: string;
  target_market?: string;
  budget?: number;
  business_model?: string;
  industry?: string;
};

export type BackendAnalysisResponse = {
  idea?: string;
  market_analysis?: {
    target_audience?: string;
    market_demand?: string;
    challenges?: string[];
  };
  revenue_analysis?: {
    pricing_model?: string;
    revenue_streams?: string[];
  };
  swot_analysis?: {
    strengths?: string[];
    weaknesses?: string[];
    opportunities?: string[];
    threats?: string[];
  };
  startup_score?: {
    overall_score?: number;
    market_score?: number;
    revenue_score?: number;
    scalability_score?: number;
    risk_score?: number;
    recommendation?: string;
  };
  recommendation?: string;
};
