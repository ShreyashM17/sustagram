module.exports = {
  content: [
    // Global template directory
    '../../templates/**/*.html',

    // App-level templates (if any)
    '../../*/templates/**/*.html',

    // Optional: for inline class usage in JS or Python
    '../../**/*.py',
    '../../**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
