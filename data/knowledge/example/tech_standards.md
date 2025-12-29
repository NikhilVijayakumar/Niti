# # NITI Technical Standards & Quality Gate

## ## 1. Architecture & Patterns
- **Pattern:** Model-View-Controller (MVC) or Layered Architecture.
- **Folder Structure:** - `/src/components` (Re-usable UI)
  - `/src/services` (API calls & Logic)
  - `/src/hooks` (Custom React logic)
- **State Management:** Use Context API for simple state, Redux Toolkit for complex global state.

## ## 2. Coding Best Practices
- **Naming:** camelCase for variables/functions, PascalCase for components.
- **Error Handling:** Every API call must be wrapped in a `try-catch` block with a user-friendly error message.
- **Comments:** Use JSDoc headers for all utility functions.

## ## 3. Definition of Done (DoD)
A Trello task is only "Done" if:
1. Code passes `npm run lint`.
2. Component is responsive (Mobile/Desktop).
3. Logic is verified with at least one happy-path manual test.
4. No sensitive keys/secrets are hardcoded.

## ## 4. Documentation
- Every new feature must have a brief `README.md` entry in its respective folder.