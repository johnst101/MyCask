import { createContext, useContext, useEffect, useState } from 'react';
import { User } from '../types/user';

interface AuthContextType {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

export const AuthContext = createContext<AuthContextType | undefined>(
  undefined
);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  // 1. State management
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  // 2. Check if user is logged in on mount (check localStorage)
  useEffect(() => {
    const checkAuth = async () => {
      const token = localStorage.getItem('access_token');
      if (token) {
        // Token exists, verify it's valid by fetching user
        try {
          const userData = await fetchCurrentUser(token);
          setUser(userData);
        } catch (error) {
          // Token invalid, remove it
          localStorage.removeItem('access_token');
          localStorage.removeItem('refresh_token');
        }
      }
      setIsLoading(false);
    };
    checkAuth();
  }, []);

  // 3. Login function
  const login = async (email: string, password: string) => {
    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ username: email, password: password }),
      });

      if (!response.ok) throw new Error('Login failed');

      const data = await response.json();

      // Store tokens in localStorage
      localStorage.setItem('access_token', data.access_token);
      localStorage.setItem('refresh_token', data.refresh_token);

      // Fetch user data
      const userData = await fetchCurrentUser(data.access_token);
      setUser(userData);
    } catch (error) {
      throw error; // Let component handle error display
    } finally {
      setIsLoading(false);
    }
  };

  // 4. Logout function
  const logout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    setUser(null);
  };

  // 5. Value object - what we're providing
  const value = {
    user,
    isAuthenticated: !!user, // Convert to boolean
    isLoading,
    login,
    logout,
  };

  // 6. Return Provider with value
  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const context = useContext(AuthContext);

  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }

  return context;
}
