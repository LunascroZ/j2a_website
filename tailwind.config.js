/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Nunito', 'sans-serif'],
      },
      colors: {
        j2aBlue: '#1e3a8a',
        j2aLightBlue: '#eff6ff',
        j2aOrange: '#f97316',
        j2aOrangeHover: '#ea580c',
      }
    },
  },
  plugins: [],
}