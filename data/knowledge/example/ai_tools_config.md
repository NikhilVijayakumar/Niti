# # NITI AI-Augmentation Configuration

## ## 1. Approved AI Stack
- **Primary Editor:** Cursor (using @Codebase and @Docs features).
- **Secondary Tools:** Antigravity (for refactoring), Kiro (for boilerplate generation).

## ## 2. Efficiency Multipliers (AEF)
*Note: Lower value = Higher efficiency*

| Task Category | AI Gain | AEF Value |
| :--- | :--- | :--- |
| **Boilerplate** (API routes, CRUD, Folder setup) | Very High | 0.5 |
| **Unit Testing** (Generating test cases) | High | 0.6 |
| **UI/CSS** (Tailwind layouts from descriptions) | High | 0.6 |
| **Refactoring** (Cleaning old code) | Medium | 0.8 |
| **Business Logic** (Complex math/security) | Low | 1.0 |

## ## 3. Prompting Requirements
- If a task has an AEF of 0.7 or lower, the Trello card **must** include a "Recommended AI Prompt" (e.g., "Use Cursor @Context to sync this with the existing Auth service").