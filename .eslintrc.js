{
  "extends": ["eslint:recommended", "plugin:cypress/recommended"],
  "parser": "@typescript-eslint/parser",
  "plugins": ["@typescript-eslint", "cypress"],
  "rules": {
    "max-len": ["error", 200],
    "semi": ["error", "always"],
    "quotes": [2, "double"],
    "prefer-const": [
      "error",
      {
        "destructuring": "any",
        "ignoreReadBeforeAssign": false
      }
    ],
    "spaced-comment": [
      "error",
      "always",
      {
        "markers": ["/"]
      }
    ],
    "prefer-arrow-callback": ["error"],
    "object-shorthand": ["error"],
    "indent": ["error", 2],
    "no-trailing-spaces": ["error"],
    "no-unused-vars": [
      "error",
      {
        "args": "none"
      }
    ],
    "eol-last": ["warn", "always"]
  },
  "globals": {
    "localStorage": "readonly",
    "setTimeout": "readonly",
    "console": "writable",
    "process": "readonly",
    "Tabulator": "readonly",
    "Axios": "readonly",
    "Blob": "readonly",
    "FormData": "readonly",
    "require": "readonly"
  }
}