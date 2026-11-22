import type { BackendAnalysisResponse, LoginPayload, StartupIdeaPayload } from './types';

const API_BASE_URL = 'http://localhost:8000';

export type SignupPayload = {
  name: string;
  email: string;
  password: string;
};

export async function signupUser(payload: SignupPayload): Promise<{ success: boolean; message: string; user_id: number }> {
  const response = await fetch(`${API_BASE_URL}/signup`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });

  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(data.detail || 'Signup failed');
  }
  return data;
}

export async function loginUser(payload: LoginPayload): Promise<{ access_token: string; token_type: string }> {
  const response = await fetch(`${API_BASE_URL}/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });

  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(data.detail || 'Login failed');
  }

  return data;
}

export async function submitIdea(payload: StartupIdeaPayload, accessToken: string): Promise<BackendAnalysisResponse & { result?: BackendAnalysisResponse }> {
  const response = await fetch(`${API_BASE_URL}/analyze`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${accessToken}`,
    },
    body: JSON.stringify(payload),
  });

  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(data.detail || 'Analysis request failed');
  }

  return data;
}
