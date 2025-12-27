/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      // Design Token System for MyCask

      // Spacing Scale - Based on 4px base unit (0.25rem)
      // This ensures consistent spacing throughout the application
      spacing: {
        // Semantic spacing tokens for common use cases
        'card-padding-xs': '1rem', // 16px - Small card padding
        'card-padding-sm': '1.5rem', // 24px - Medium card padding
        'card-padding-md': '2rem', // 32px - Large card padding

        'section-gap-xs': '0.75rem', // 12px - Tight spacing between form fields
        'section-gap-sm': '1rem', // 16px - Default spacing between form fields
        'section-gap-md': '1.5rem', // 24px - Medium spacing between sections

        'content-margin-xs': '1rem', // 16px - Small vertical margins
        'content-margin-sm': '1.5rem', // 24px - Medium vertical margins
        'content-margin-md': '2rem', // 32px - Large vertical margins

        'heading-margin-sm': '1rem', // 16px - Small heading bottom margin
        'heading-margin-md': '1.5rem', // 24px - Medium heading bottom margin
      },

      // Breakpoints - Including container query breakpoints
      screens: {
        // Standard responsive breakpoints
        sm: '640px',
        md: '768px',
        lg: '1024px',
        xl: '1280px',
        '2xl': '1536px',
      },

      // Container query breakpoints (used with @container)
      container: {
        sm: '400px',
        md: '600px',
        lg: '800px',
      },

      // Typography Scale
      fontSize: {
        // Base font sizes with responsive scaling
        'heading-xs': ['1rem', { lineHeight: '1.5', letterSpacing: '-0.01em' }], // 16px
        'heading-sm': [
          '1.25rem',
          { lineHeight: '1.4', letterSpacing: '-0.02em' },
        ], // 20px
        'heading-md': [
          '1.5rem',
          { lineHeight: '1.3', letterSpacing: '-0.02em' },
        ], // 24px
        'heading-lg': ['2rem', { lineHeight: '1.2', letterSpacing: '-0.03em' }], // 32px
        'heading-xl': [
          '2.5rem',
          { lineHeight: '1.2', letterSpacing: '-0.03em' },
        ], // 40px

        // Body text
        'body-sm': ['0.875rem', { lineHeight: '1.5' }], // 14px
        'body-base': ['1rem', { lineHeight: '1.5' }], // 16px
        'body-lg': ['1.125rem', { lineHeight: '1.5' }], // 18px
      },

      // Font Families
      fontFamily: {
        'playfair-display': ['Playfair Display', 'serif'],
        inter: ['Inter', 'sans-serif'],
        primary: ['Inter', 'sans-serif'],
        accent: ['Playfair Display', 'serif'],
      },

      // Border Radius
      borderRadius: {
        input: '0.375rem', // 6px - Standard input border radius
        card: '0.375rem', // 6px - Card border radius
        button: '0.375rem', // 6px - Button border radius
        icon: '9999px', // Full circle for icons
      },

      // Border Width
      borderWidth: {
        input: '2px', // Standard input border width
        focus: '2px', // Focus ring border width
      },

      // Max Widths for Containers
      maxWidth: {
        'card-sm': '28rem', // 448px - Small card max width
        'card-md': '32rem', // 512px - Medium card max width
        'card-lg': '36rem', // 576px - Large card max width
        'card-xl': '42rem', // 672px - Extra large card max width
      },

      // Heights for Viewport Calculations
      height: {
        'viewport-offset-xs': 'calc(100vh - 2rem)', // 32px offset
        'viewport-offset-sm': 'calc(100vh - 3rem)', // 48px offset
        'viewport-offset-md': 'calc(100vh - 4rem)', // 64px offset
      },

      // Colors - These extend the colors defined in index.css @theme
      // The actual color values are in CSS, but we can reference them here
      colors: {
        // Brand colors are defined in index.css via @theme
        // This section can be used to add additional semantic color tokens if needed
      },

      // Box Shadow
      boxShadow: {
        'input-focus': '0 0 0 2px rgba(196, 154, 59, 0.2)', // Focus ring for inputs
        card: '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)',
        'card-hover':
          '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
      },

      // Transition Durations
      transitionDuration: {
        fast: '150ms',
        base: '200ms',
        slow: '300ms',
      },

      // Z-Index Scale
      zIndex: {
        dropdown: '1000',
        sticky: '1020',
        fixed: '1030',
        'modal-backdrop': '1040',
        modal: '1050',
        popover: '1060',
        tooltip: '1070',
      },
    },
  },
  plugins: [],
};
