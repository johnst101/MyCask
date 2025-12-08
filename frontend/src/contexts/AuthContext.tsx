import { createContext, useContext, useEffect, useState } from 'react';
import { User } from '../types/user';
import { fetchCurrentUser, loginUser } from '../services/authService';

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
          const userData = await fetchCurrentUser();
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
      const data = await loginUser(email, password);
      localStorage.setItem('access_token', data.access_token);
      localStorage.setItem('refresh_token', data.refresh_token);
      const userData = await fetchCurrentUser(); // ✅ No token needed!
      setUser(userData);
    } catch (error) {
      throw error;
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
