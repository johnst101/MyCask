import { useState } from 'react';
import SubmitButton from './SubmitButton';
import mc_logo from '../assets/mc_logo-removebg.png';

const Login = () => {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [loginError, setLoginError] = useState(false);

  return (
    <div className="@container bg-white rounded-md w-full max-w-md mx-auto my-4 sm:my-6 md:my-8 px-4 py-4 sm:px-6 sm:py-6 md:px-8 md:py-8">
      <img
        src={mc_logo}
        alt="MyCask Logo"
        className="w-30 h-30 @[400px]:w-40 @[400px]:h-40 @[600px]:w-50 @[600px]:h-50 mx-auto mb-4"
      />
      <h1 className="font-playfair-display font-bold text-xl @[400px]:text-2xl @[600px]:text-3xl text-center text-deep-green mb-4 sm:mb-6">
        Login to MyCask
      </h1>
      <form
        //onSubmit={handleSubmit}
        className="flex flex-col gap-3 @[400px]:gap-4 text-deep-green"
      >
        <input
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full px-3 py-2.5 @[400px]:px-4 @[400px]:py-3 text-base border-2 border-luxury-gold rounded-md focus:outline-none focus:ring-2 focus:ring-luxury-gold focus:border-luxury-gold disabled:opacity-50 disabled:cursor-not-allowed"
          type="email"
          placeholder="Email"
          required
          //disabled={isLoading}
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
          //disabled={isLoading}
        />

        <SubmitButton
          isLoading={isLoading}
          loadingText="Logging in..."
          defaultText="Login"
          //disabled={!isFormValid}
        />
        <div className="text-error text-sm px-2" hidden={!loginError}>
          Invalid email or password. Please try again.
        </div>
      </form>
    </div>
  );
};

export default Login;
