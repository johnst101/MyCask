import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { registerUser } from '../services/authService';
import PasswordRequirements, {
  checkPasswordRequirements,
} from './PasswordRequirements';
import SubmitButton from './SubmitButton';

const Signup = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [isPasswordFocused, setIsPasswordFocused] = useState(false);
  const [emailError, setEmailError] = useState(false);
  const [usernameError, setUsernameError] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);

  const isFormValid =
    checkPasswordRequirements(password) && password === confirmPassword;

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!isFormValid || isLoading) {
      return;
    }
    setIsLoading(true);
    setEmailError(false);
    setUsernameError(false);
    try {
      const response = await registerUser(
        email,
        password,
        username,
        firstName,
        lastName
      );
      if (response) {
        setIsSuccess(true);
        // Redirect to login page after 2 seconds
        // TODO: eventually create more dyanmic, fun, and creative transition animations
        setTimeout(() => {
          navigate('/login');
        }, 1500);
      }
    } catch (error) {
      if (
        error instanceof Error &&
        error.message.includes('Email already registered')
      ) {
        setEmailError(true);
        setUsernameError(false);
      } else if (
        error instanceof Error &&
        error.message.includes('Username already taken')
      ) {
        setUsernameError(true);
        setEmailError(false);
      }
    } finally {
      setIsLoading(false);
    }
  };
  // Success message view
  if (isSuccess) {
    return (
      <div className="@container bg-white rounded-md w-full max-w-md mx-auto my-4 sm:my-6 md:my-8 px-4 py-4 sm:px-6 sm:py-6 md:px-8 md:py-8 max-h-[calc(100vh-2rem)] sm:max-h-[calc(100vh-3rem)] md:max-h-[calc(100vh-4rem)] overflow-y-auto">
        <div className="flex flex-col items-center justify-center py-8 animate-fade-in">
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
            Account Created Successfully!
          </h2>
          <p className="text-center text-text-secondary mb-4">
            Redirecting to login page...
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="@container bg-white rounded-md w-full max-w-md mx-auto my-4 sm:my-6 md:my-8 px-4 py-4 sm:px-6 sm:py-6 md:px-8 md:py-8 max-h-[calc(100vh-2rem)] sm:max-h-[calc(100vh-3rem)] md:max-h-[calc(100vh-4rem)] overflow-y-auto animate-fade-in">
      <h1 className="font-playfair-display font-bold text-xl @[400px]:text-2xl @[600px]:text-3xl text-center text-deep-green mb-4 sm:mb-6">
        Join the MyCask community
      </h1>
      <form
        onSubmit={handleSubmit}
        className="flex flex-col gap-3 @[400px]:gap-4 text-deep-green"
      >
        <div className="relative">
          <span className="absolute top-1 left-2 text-red-500 text-sm font-bold z-10">
            *
          </span>
          <input
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full px-3 py-2.5 @[400px]:px-4 @[400px]:py-3 text-base border-2 border-luxury-gold rounded-md focus:outline-none focus:ring-2 focus:ring-luxury-gold focus:border-luxury-gold disabled:opacity-50 disabled:cursor-not-allowed"
            type="email"
            placeholder="Email"
            required
            disabled={isLoading}
          />
        </div>
        <div className="text-error text-sm px-2" hidden={!emailError}>
          Account with this email already exists. Please use a different email.
        </div>
        <input
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="px-3 py-2.5 @[400px]:px-4 @[400px]:py-3 text-base border-2 border-luxury-gold rounded-md focus:outline-none focus:ring-2 focus:ring-luxury-gold focus:border-luxury-gold disabled:opacity-50 disabled:cursor-not-allowed"
          type="text"
          placeholder="Username"
          disabled={isLoading}
        />
        <div className="text-error text-sm px-2" hidden={!usernameError}>
          Account with this username already exists. Please use a different
          username.
        </div>
        <input
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
          className="px-3 py-2.5 @[400px]:px-4 @[400px]:py-3 text-base border-2 border-luxury-gold rounded-md focus:outline-none focus:ring-2 focus:ring-luxury-gold focus:border-luxury-gold disabled:opacity-50 disabled:cursor-not-allowed"
          type="text"
          placeholder="First Name"
          disabled={isLoading}
        />
        <input
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
          className="px-3 py-2.5 @[400px]:px-4 @[400px]:py-3 text-base border-2 border-luxury-gold rounded-md focus:outline-none focus:ring-2 focus:ring-luxury-gold focus:border-luxury-gold disabled:opacity-50 disabled:cursor-not-allowed"
          type="text"
          placeholder="Last Name"
          disabled={isLoading}
        />
        <div
          className={`relative transition-all duration-200 ${
            isPasswordFocused ? 'mb-28 @[400px]:mb-32' : ''
          }`}
        >
          <span className="absolute top-1 left-2 text-red-500 text-sm font-bold z-10">
            *
          </span>
          <input
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            onFocus={() => setIsPasswordFocused(true)}
            onBlur={() => setIsPasswordFocused(false)}
            className="w-full px-3 py-2.5 @[400px]:px-4 @[400px]:py-3 text-base border-2 border-luxury-gold rounded-md focus:outline-none focus:ring-2 focus:ring-luxury-gold focus:border-luxury-gold disabled:opacity-50 disabled:cursor-not-allowed"
            type="password"
            placeholder="Password"
            required
            disabled={isLoading}
          />
          {isPasswordFocused && <PasswordRequirements password={password} />}
        </div>
        <div className="relative">
          <span className="absolute top-1 left-2 text-red-500 text-sm font-bold z-10">
            *
          </span>
          <input
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            className="w-full px-3 py-2.5 @[400px]:px-4 @[400px]:py-3 text-base border-2 border-luxury-gold rounded-md focus:outline-none focus:ring-2 focus:ring-luxury-gold focus:border-luxury-gold disabled:opacity-50 disabled:cursor-not-allowed"
            type="password"
            placeholder="Confirm Password"
            required
            disabled={isLoading}
          />
        </div>
        {password !== confirmPassword && (
          <div className="text-error text-sm px-2">Passwords must match.</div>
        )}
        <SubmitButton
          isLoading={isLoading}
          loadingText="Creating account..."
          defaultText="Create account"
          disabled={!isFormValid}
        />
      </form>
    </div>
  );
};

export default Signup;
