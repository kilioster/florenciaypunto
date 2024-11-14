/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["*.{html,js}"],
  theme: {
    container: {
      padding: {
        DEFAULT: '15px',
      },
    },
    screens: {
      sm: '640px',
      md: '768px',
      lg: '1024px',
      xl: '1280px',
    },
    fontFamily: {
      primary: 'DM Serif Display',
      secondary: 'Jost',
    },
    backgroundImage: {
      hero: 'url(./media/hero/bg.webp)',
      //grid: 'url(../assets/grid.png)',
    },
    extend: {
      colors: {
        primary: {
          DEFAULT: '#292f36',
          hover: '#343e4a',
        },
        secondary: '#4d5053',
        accent: {
          DEFAULT: '#cda274',
          secondary: '#f4f8ec',
          hover: '#b88c5d',
        },
      }
    },
  },
  plugins: [],
}

