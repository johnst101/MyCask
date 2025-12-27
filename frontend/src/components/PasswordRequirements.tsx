import React from 'react';

interface PasswordRequirementsProps {
  password: string;
}

export const checkPasswordRequirements = (password: string): boolean => {
  return (
    password.length >= 8 &&
    /[A-Z]/.test(password) &&
    /[a-z]/.test(password) &&
    /[0-9]/.test(password) &&
    /[^A-Za-z0-9 ]/.test(password)
  );
};

const PasswordRequirements: React.FC<PasswordRequirementsProps> = ({
  password,
}) => {
  const requirements = [
    {
      text: 'At least 8 characters long',
      met: password.length >= 8,
    },
    {
      text: 'At least one uppercase letter',
      met: /[A-Z]/.test(password),
    },
    {
      text: 'At least one lowercase letter',
      met: /[a-z]/.test(password),
    },
    {
      text: 'At least one number',
      met: /[0-9]/.test(password),
    },
    {
      text: 'At least one special character',
      met: /[^A-Za-z0-9 ]/.test(password),
    },
  ];

  return (
    <div className="absolute top-full left-0 right-0 mt-2 z-30 bg-white border-2 border-luxury-gold rounded-md shadow-lg p-3 @[400px]:p-4">
      {/* Arrow pointing to input */}
      <div className="absolute -top-2 left-4 w-4 h-4 bg-white border-l-2 border-t-2 border-luxury-gold transform rotate-45"></div>

      <p className="text-xs font-semibold text-deep-green mb-2">
        Password Requirements:
      </p>
      <ul className="text-xs space-y-0.5">
        {requirements.map((requirement, index) => (
          <li
            key={index}
            className={`flex items-start ${
              requirement.met ? 'text-success' : 'text-gray-500'
            }`}
          >
            <span className="mr-2 mt-0.5 shrink-0">
              {requirement.met ? '✅' : '❌'}
            </span>
            <span>{requirement.text}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PasswordRequirements;
