/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['../templates/*.{html,js}',],
  theme: {
    extend: {
      fontFamily: {
        'prim': ['Geared Slab', 'sans-serif'], 
        'sec': ['National', 'serif']
      },
      colors: {
        primary: "#22223B", 
        sec: "#4A4E69", 
        sealight: "#E9F7F2", 
        sea: "#F15025", 
        accent: "#6E8894"
      }
    },
  },
  plugins: [],
}
