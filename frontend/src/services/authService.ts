import { User } from '../types/user';
import { Token } from '../types/token';
import { apiRequest } from '../utils/api';

const API_BASE_URL = import.meta.env.VITE_API_URL;

/**
 * Fetch current user data from the API
 * Requeires valid access token in localStorage
 */
export async function fetchCurrentUser(): Promise<User> {
  // TODO: Implement this
}

/**
 * Login user and return tokens
 */
export async function loginUser(
  email: string,
  password: string
): Promise<Token> {
  // TODO: Implement this
}
