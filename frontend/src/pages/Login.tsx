import { useState } from 'react';
import SubmitButton from '../components/SubmitButton';
import mc_logo from '../assets/mc_logo-removebg.png';
import { loginUser } from '../services/authService';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  // const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [loginError, setLoginError] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);
  const [isNavigating, setIsNavigating] = useState(false);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (isLoading) {
      return;
    }
    setIsLoading(true);
    setLoginError(false);
    try {
      const response = await loginUser(email, password);
      if (response) {
        setIsSuccess(true);
        setIsNavigating(true);
        // TODO: eventually create more dyanmic, fun, and creative transition animations
        setTimeout(() => {
          navigate('/profile');
        }, 1000);
      }
    } catch (error) {
      setLoginError(true);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSignupClick = (e: React.MouseEvent<HTMLAnchorElement>) => {
    e.preventDefault();
    setIsNavigating(true);
    // Wait for fade-out animation to complete before navigating
    setTimeout(() => {
      navigate('/signup');
    }, 400);
  };

  if (isSuccess) {
    return (
      <div className="@container bg-white rounded-md w-full max-w-md md:max-w-lg lg:max-w-xl mx-auto my-4 sm:my-6 md:my-8 px-4 py-4 sm:px-6 sm:py-6 md:px-8 md:py-8 max-h-[calc(100vh-2rem)] sm:max-h-[calc(100vh-3rem)] md:max-h-[calc(100vh-4rem)] overflow-y-auto">
        <div className="flex flex-col items-center justify-center py-8">
          <div className="w-16 h-16 @[400px]:w-20 @[400px]:h-20 rounded-full bg-success flex items-center justify-center mb-4 animate-scale-in">
            <svg
              className="w-8 h-8 @[400px]:w-10 @[400px]:h-10 text-white"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={3}
                d="M5 13l4 4L19 7"
              />
            </svg>
          </div>
          <h2 className="font-playfair-display font-bold text-xl @[400px]:text-2xl @[600px]:text-3xl text-center text-deep-green mb-2">
            Login Successful!
          </h2>
        </div>
      </div>
    );
  }

  return (
    <div
      className={`@container bg-white rounded-md w-full max-w-md md:max-w-lg lg:max-w-xl mx-auto my-4 sm:my-6 md:my-8 px-4 py-4 sm:px-6 sm:py-6 md:px-8 md:py-8 ${isNavigating ? 'animate-fade-out' : 'animate-fade-in'}`}
    >
      <img
        src={mc_logo}
        alt="MyCask Logo"
        className="w-30 h-30 @[400px]:w-40 @[400px]:h-40 @[600px]:w-50 @[600px]:h-50 mx-auto mb-4"
      />
      <h1 className="font-playfair-display font-bold text-xl @[400px]:text-2xl @[600px]:text-3xl text-center text-deep-green mb-4 sm:mb-6">
        Login to MyCask
      </h1>
      <form
        onSubmit={handleSubmit}
        className="flex flex-col gap-3 @[400px]:gap-4 text-deep-green"
      >
        <input
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full px-3 py-2.5 @[400px]:px-4 @[400px]:py-3 text-base border-2 border-luxury-gold rounded-md focus:outline-none focus:ring-2 focus:ring-luxury-gold focus:border-luxury-gold disabled:opacity-50 disabled:cursor-not-allowed"
          type="email"
          placeholder="Email"
          required
          disabled={isLoading}
        />
        <input
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          //onFocus={() => setIsPasswordFocused(true)}
          //onBlur={() => setIsPasswordFocused(false)}
          className="w-full px-3 py-2.5 @[400px]:px-4 @[400px]:py-3 text-base border-2 border-luxury-gold rounded-md focus:outline-none focus:ring-2 focus:ring-luxury-gold focus:border-luxury-gold disabled:opacity-50 disabled:cursor-not-allowed"
          type="password"
          placeholder="Password"
          required
          disabled={isLoading}
        />
        <div className="text-error text-sm px-2" hidden={!loginError}>
          Invalid email or password. Please try again.
        </div>
        <SubmitButton
          isLoading={isLoading}
          loadingText="Logging in..."
          defaultText="Login"
        />
      </form>
      <div className="flex justify-around text-center text-sm text-text-secondary mt-2">
        {/* TODO: eventually create forgot password and forgot email pages */}
        <a href="/forgot-password">Forgot password?</a>
        <a href="/reset-password">Forgot email?</a>
      </div>
      <div className="text-center text-md mt-4">
        <a href="/signup" onClick={handleSignupClick}>
          Don't have an account? Sign up
        </a>
      </div>
    </div>
  );
};

export default Login;
