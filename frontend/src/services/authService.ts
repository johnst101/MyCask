import { User } from '../types/user';
import { Token } from '../types/token';
import { apiRequest } from '../utils/api';

const API_BASE_URL = import.meta.env.VITE_API_URL;

/**
 * Fetch current user data from the API
 * Requeires valid access token in localStorage
 */
export async function fetchCurrentUser(): Promise<User> {
  return apiRequest<User>('/users/me');
}

/**
 * Login user and return tokens
 */
export async function loginUser(
  email: string,
  password: string
): Promise<Token> {
  return apiRequest<Token>('/auth/login', {
    method: 'POST',
    useFormData: true,
    formData: new URLSearchParams({ username: email, password }),
  });
}

/**
 * Register a new user
 */
export async function registerUser(
  email: string,
  password: string,
  username?: string,
  first_name?: string,
  last_name?: string
): Promise<User> {
  return apiRequest<User>('/auth/register', {
    method: 'POST',
    body: JSON.stringify({
      email,
      password,
      username,
      first_name,
      last_name,
    }),
  });
}

/**
 * Refresh access token using refresh token
 */
export async function refreshToken(refreshToken: string): Promise<Token> {
  return apiRequest<Token>('/auth/refresh', {
    method: 'POST',
    body: JSON.stringify({ refresh_token: refreshToken }),
  });
}
