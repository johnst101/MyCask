interface SubmitButtonProps {
  isLoading: boolean;
  loadingText: string;
  defaultText: string;
  disabled?: boolean;
  type?: 'button' | 'submit' | 'reset';
  className?: string;
}

const SubmitButton = ({
  isLoading,
  loadingText,
  defaultText,
  disabled = false,
  type = 'submit',
  className = '',
}: SubmitButtonProps) => {
  return (
    <button
      className={`font-playfair-display px-4 py-2.5 @[400px]:px-6 @[400px]:py-3 text-base @[400px]:text-lg mt-2 mb-2 @[400px]:mb-4 bg-deep-green text-white border-2 border-deep-green rounded-md hover:bg-opacity-90 active:bg-opacity-80 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2 ${className}`}
      type={type}
      disabled={disabled || isLoading}
    >
      {isLoading && (
        <svg
          className="animate-spin h-5 w-5 text-white"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
        >
          <circle
            className="opacity-25"
            cx="12"
            cy="12"
            r="10"
            stroke="currentColor"
            strokeWidth="4"
          ></circle>
          <path
            className="opacity-75"
            fill="currentColor"
            d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
          ></path>
        </svg>
      )}
      {isLoading ? loadingText : defaultText}
    </button>
  );
};

export default SubmitButton;
