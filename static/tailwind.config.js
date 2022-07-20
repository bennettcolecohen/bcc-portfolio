/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['../templates/*.{html,js}',],
  theme: {
    extend: {
      fontFamily: {
        'slab': ['Geared Slab', 'sans-serif']
      },
      colors: {
        cyan: {
          150: '#d1e8eb',
        },
      }
    },
  },
  plugins: [],
}
