import { useState, useEffect } from 'react';
import SubmitButton from '../components/SubmitButton';
import logo from '../assets/mc_logo-removebg.png';
import { useAuth } from '../contexts/AuthContext';

const Profile = () => {
  const { user, isLoading: authLoading } = useAuth();
  const [email, setEmail] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [username, setUsername] = useState('');

  // Populate form fields when user data is available
  useEffect(() => {
    if (user) {
      setEmail(user.email || '');
      setFirstName(user.first_name || '');
      setLastName(user.last_name || '');
      setUsername(user.username || '');
    }
  }, [user]);

  if (authLoading) {
    return (
      <div className="card-container animate-fade-in">
        <div className="flex justify-center items-center py-8">
          <p>Loading...</p>
        </div>
      </div>
    );
  }

  if (!user) {
    return (
      <div className="card-container animate-fade-in">
        <div className="flex justify-center items-center py-8">
          <p>Please log in to view your profile.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="card-container animate-fade-in">
      <div className="flex justify-between items-center">
        <h1 className="heading-profile">
          <span className="font-playfair-display font-light text-text-secondary text-xl @[400px]:text-2xl @[600px]:text-3xl">
            Hello,
          </span>{' '}
          <br />
          {user.first_name || 'User'}
        </h1>
        <img src={logo} alt="MyCask Logo" className="profile-picture" />{' '}
        {/* TODO: add ability to change profile picture */}
      </div>
      <form className="form-container">
        <input
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="form-input"
          type="email"
          placeholder="Current Email"
        />
        <input
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
          className="form-input"
          type="text"
          placeholder="Current First Name"
        />
        <input
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
          className="form-input"
          type="text"
          placeholder="Current Last Name"
        />
        <input
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="form-input"
          type="text"
          placeholder="Current Username"
        />
        <button className="password-reset-button">
          Update Password
          {/* TODO: add redirect to password reset page */}
        </button>
        <SubmitButton
          isLoading={false}
          loadingText="Updating profile..."
          defaultText="Update Profile"
        />
        {/* TODO: button is disabled unless something is changed in the form */}
      </form>
      <div className="flex justify-center items-center mt-4">
        <a href="/delete-account" className="text-error">
          Delete Account
        </a>
        {/* TODO: add ability to delete account */}
      </div>
    </div>
  );
};

export default Profile;
