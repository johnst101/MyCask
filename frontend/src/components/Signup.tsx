const Signup = () => {
  return (
    <div className="bg-white rounded-md">
      <h1 className="font-playfair-display font-bold text-2xl text-center text-deep-green m-4">
        Create your account
      </h1>
      <form className="flex flex-col gap-4 ml-8 mr-8 text-deep-green">
        <input
          className="px-4 py-2 border-2 border-luxury-gold rounded-md"
          type="email"
          placeholder="Email"
          required
        />
        <input
          className="px-4 py-2 border-2 border-luxury-gold rounded-md"
          type="text"
          placeholder="Username"
        />
        <input
          className="px-4 py-2 border-2 border-luxury-gold rounded-md"
          type="text"
          placeholder="First Name"
        />
        <input
          className="px-4 py-2 border-2 border-luxury-gold rounded-md"
          type="text"
          placeholder="Last Name"
        />
        <input
          className="px-4 py-2 border-2 border-luxury-gold rounded-md"
          type="password"
          placeholder="Password"
          required
        />
        <input
          className="px-4 py-2 border-2 border-luxury-gold rounded-md"
          type="password"
          placeholder="Confirm Password"
          required
        />
        <button
          className="btn font-playfair-display px-4 py-2 text-lg mb-4 bg-deep-green text-white border-2 border-deep-green rounded-md"
          type="submit"
        >
          Create account
        </button>
      </form>
    </div>
  );
};

export default Signup;
