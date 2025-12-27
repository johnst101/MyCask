const Profile = () => {
  return (
    <div className="@container bg-white rounded-md w-full max-w-md md:max-w-lg lg:max-w-xl mx-auto my-4 sm:my-6 md:my-8 px-4 py-4 sm:px-6 sm:py-6 md:px-8 md:py-8 max-h-[calc(100vh-2rem)] sm:max-h-[calc(100vh-3rem)] md:max-h-[calc(100vh-4rem)] overflow-y-auto">
      <div className="flex flex-col items-center justify-center py-8">
        <h1 className="font-playfair-display font-bold text-xl @[400px]:text-2xl @[600px]:text-3xl text-center text-deep-green mb-4 sm:mb-6">
          Profile
        </h1>
      </div>
    </div>
  );
};

export default Profile;
