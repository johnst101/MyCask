import { useState, useEffect } from 'react';
import SubmitButton from '../components/SubmitButton';
import logo from '../assets/mc_logo-removebg.png';
import { useAuth } from '../contexts/AuthContext';

const Profile = () => {
  const { user } = useAuth();
  const [email, setEmail] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [username, setUsername] = useState('');
  const [isFormDirty, setIsFormDirty] = useState(false);

  useEffect(() => {
    if (user) {
      setEmail(user.email || '');
      setFirstName(user.first_name || '');
      setLastName(user.last_name || '');
      setUsername(user.username || '');
    }
  }, [user]);

  return (
    <div className="card-container animate-fade-in">
      <div className="flex justify-between items-center">
        <h1 className="heading-profile">
          <span className="font-playfair-display font-light text-text-secondary text-xl @[400px]:text-2xl @[600px]:text-3xl">
            Hello,
          </span>{' '}
          <br />
          {user?.first_name ? user.first_name : 'User'}
        </h1>
        <img src={logo} alt="MyCask Logo" className="profile-picture" />{' '}
        {/* TODO: add ability to change profile picture; need api endpoint */}
      </div>
      <form className="flex flex-col color-deep-green">
        <label htmlFor="email" className="form-label">
          Email
        </label>
        <input
          value={email}
          onChange={(e) => {
            setEmail(e.target.value);
            if (e.target.value !== user?.email) {
              setIsFormDirty(true);
            } else {
              setIsFormDirty(false);
            }
          }}
          className="form-input mb-2 @[400px]:mb-4"
          type="email"
          id="email"
        />
        <label htmlFor="first_name" className="form-label">
          First Name
        </label>
        <input
          value={firstName}
          onChange={(e) => {
            setFirstName(e.target.value);
            if (e.target.value !== user?.first_name) {
              setIsFormDirty(true);
            } else {
              setIsFormDirty(false);
            }
          }}
          className="form-input mb-2 @[400px]:mb-4"
          type="text"
          placeholder="First Name"
          id="first_name"
        />
        <label htmlFor="last_name" className="form-label">
          Last Name
        </label>
        <input
          value={lastName}
          onChange={(e) => {
            setLastName(e.target.value);
            if (e.target.value !== user?.last_name) {
              setIsFormDirty(true);
            } else {
              setIsFormDirty(false);
            }
          }}
          className="form-input mb-2 @[400px]:mb-4"
          type="text"
          placeholder="Last Name"
          id="last_name"
        />
        <label htmlFor="username" className="form-label">
          Username
        </label>
        <input
          value={username}
          onChange={(e) => {
            setUsername(e.target.value);
            if (e.target.value !== user?.username) {
              setIsFormDirty(true);
            } else {
              setIsFormDirty(false);
            }
          }}
          className="form-input mb-4 @[400px]:mb-6"
          type="text"
          placeholder="Username"
          id="username"
        />
        <button className="password-reset-button mb-2 @[400px]:mb-4">
          Update Password
          {/* TODO: add redirect to password reset page; need api endpoint */}
        </button>
        <SubmitButton
          isLoading={false}
          loadingText="Updating profile..."
          defaultText="Update Profile"
          disabled={!isFormDirty}
        />
        {/* TODO: add ability to update changes to the fields; need api endpoint */}
      </form>
      <div className="flex justify-center items-center mt-4">
        <a href="/delete-account" className="text-error">
          Delete Account
        </a>
        {/* TODO: add ability to delete account; need api endpoint */}
      </div>
    </div>
  );
};

export default Profile;
