import type { BackendAnalysisResponse, LoginPayload, StartupIdeaPayload } from './types';

const API_BASE_URL = 'http://localhost:8000';

export async function loginUser(payload: LoginPayload): Promise<{ token: string }> {
  const response = await fetch(`${API_BASE_URL}/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error('Login failed');
  }

  return response.json();
}

export async function submitIdea(payload: StartupIdeaPayload): Promise<BackendAnalysisResponse> {
  const response = await fetch(`${API_BASE_URL}/analyze`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error('Analysis request failed');
  }

  return response.json();
}
