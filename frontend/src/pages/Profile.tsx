import { useParams } from 'react-router-dom';
import SubmitButton from '../components/SubmitButton';
import logo from '../assets/mc_logo-removebg.png';

const Profile = () => {
  const { firstName } = useParams<{ firstName: string }>(); // FIXME: is this necessary? Can I just get the username from the JWT token?
  // TODO: get user profile data from backend based on who is logged in (from JWT token? How else should I get this information?)

  return (
    <div className="card-container animate-fade-in">
      <div className="flex justify-between items-center">
        <h1 className="heading-profile">
          <span className="font-playfair-display font-light text-text-secondary text-xl @[400px]:text-2xl @[600px]:text-3xl">
            Hello,
          </span>{' '}
          <br />
          {firstName || 'User'}
        </h1>
        <img src={logo} alt="MyCask Logo" className="profile-picture" />
      </div>
      <form className="form-container">
        <input
          className="form-input"
          type="email"
          placeholder="Current Email"
        />
        <input
          className="form-input"
          type="text"
          placeholder="Current First Name"
        />
        <input
          className="form-input"
          type="text"
          placeholder="Current Last Name"
        />
        <input
          className="form-input"
          type="text"
          placeholder="Current Username"
        />
        <button className="password-reset-button">
          Update Password (add redirect to password reset page)
        </button>
        <SubmitButton
          isLoading={false}
          loadingText="Updating profile..."
          defaultText="Update Profile"
        />
      </form>
      <div className="flex justify-center items-center mt-4">
        <a href="/delete-account" className="text-red-500">
          Delete Account
        </a>
      </div>
    </div>
  );
};

export default Profile;
