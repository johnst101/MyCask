import { useState } from 'react';
import { registerUser } from '../services/authService';
import PasswordRequirements, {
  checkPasswordRequirements,
} from './PasswordRequirements';

const Signup = () => {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [isPasswordFocused, setIsPasswordFocused] = useState(false);
  const [emailError, setEmailError] = useState(false);
  const [usernameError, setUsernameError] = useState(false);
  const [passwordError, setPasswordError] = useState(false);

  const isFormValid =
    checkPasswordRequirements(password) && password === confirmPassword;

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!isFormValid) {
      return;
    }
    try {
      const response = await registerUser(
        email,
        password,
        username,
        firstName,
        lastName
      );
      console.log(response);
    } catch (error) {
      console.error(error);
      // TODO: update error handling to use numbers or constant values instead of checking strings
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
      } else if (
        error instanceof Error &&
        error.message.includes('Password is not strong enough')
      ) {
        setPasswordError(true);
        setEmailError(false);
        setUsernameError(false);
      }
    }
  };

  return (
    <div className="@container bg-white rounded-md w-full max-w-md mx-auto my-4 sm:my-6 md:my-8 px-4 py-4 sm:px-6 sm:py-6 md:px-8 md:py-8">
      <h1 className="font-playfair-display font-bold text-xl @[400px]:text-2xl @[600px]:text-3xl text-center text-deep-green mb-4 sm:mb-6">
        Join the MyCask community
      </h1>
      <form
        onSubmit={handleSubmit}
        className="flex flex-col gap-3 @[400px]:gap-4 text-deep-green"
      >
        <input
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="px-3 py-2.5 @[400px]:px-4 @[400px]:py-3 text-base border-2 border-luxury-gold rounded-md focus:outline-none focus:ring-2 focus:ring-luxury-gold focus:border-luxury-gold"
          type="email"
          placeholder="Email"
          required
        />
        <div className="text-error text-sm px-2" hidden={!emailError}>
          Account with this email already exists. Please use a different email.
        </div>
        <input
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="px-3 py-2.5 @[400px]:px-4 @[400px]:py-3 text-base border-2 border-luxury-gold rounded-md focus:outline-none focus:ring-2 focus:ring-luxury-gold focus:border-luxury-gold"
          type="text"
          placeholder="Username"
        />
        <div className="text-error text-sm px-2" hidden={!usernameError}>
          Account with this username already exists. Please use a different
          username.
        </div>
        <input
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
          className="px-3 py-2.5 @[400px]:px-4 @[400px]:py-3 text-base border-2 border-luxury-gold rounded-md focus:outline-none focus:ring-2 focus:ring-luxury-gold focus:border-luxury-gold"
          type="text"
          placeholder="First Name"
        />
        <input
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
          className="px-3 py-2.5 @[400px]:px-4 @[400px]:py-3 text-base border-2 border-luxury-gold rounded-md focus:outline-none focus:ring-2 focus:ring-luxury-gold focus:border-luxury-gold"
          type="text"
          placeholder="Last Name"
        />
        <div className="relative">
          <input
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            onFocus={() => setIsPasswordFocused(true)}
            onBlur={() => setIsPasswordFocused(false)}
            className="w-full px-3 py-2.5 @[400px]:px-4 @[400px]:py-3 text-base border-2 border-luxury-gold rounded-md focus:outline-none focus:ring-2 focus:ring-luxury-gold focus:border-luxury-gold"
            type="password"
            placeholder="Password"
            required
          />
          {isPasswordFocused && <PasswordRequirements password={password} />}
        </div>
        <div
          className={`transition-all duration-200 ${
            isPasswordFocused ? 'mt-32 @[400px]:mt-36' : ''
          }`}
        >
          <input
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            className="w-full px-3 py-2.5 @[400px]:px-4 @[400px]:py-3 text-base border-2 border-luxury-gold rounded-md focus:outline-none focus:ring-2 focus:ring-luxury-gold focus:border-luxury-gold"
            type="password"
            placeholder="Confirm Password"
            required
          />
        </div>
        {password !== confirmPassword && (
          <div className="text-error text-sm px-2">Passwords must match.</div>
        )}
        <button
          className="font-playfair-display px-4 py-2.5 @[400px]:px-6 @[400px]:py-3 text-base @[400px]:text-lg mt-2 mb-2 @[400px]:mb-4 bg-deep-green text-white border-2 border-deep-green rounded-md hover:bg-opacity-90 active:bg-opacity-80 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          type="submit"
          disabled={!isFormValid}
        >
          Create account
        </button>
      </form>
    </div>
  );
};

export default Signup;
