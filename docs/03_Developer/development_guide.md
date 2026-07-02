---
project: "PROJECT_NAME"
role: "Developer"
last_updated: 2026-07-02
tags:
  - role/developer
  - guidelines
  - setup
---

# 💻 Developer: Conventions & Setup Guidelines

◀️ Back to [[00_Project_Hub]] | Architecture: [[system_architecture]]

This document serves as the guide for anyone (human or AI) writing code in this repository. Follow these conventions strictly.

---

## 🚀 Local Development Setup
*Instructions to get the workspace up and running.*
1. **Prerequisites**: Node.js v18+, PostgreSQL v15+
2. **Install Dependencies**:
   ```bash
   npm install
   ```
3. **Environment Setup**: Copy `.env.example` to `.env` and fill in secrets.
4. **Run Dev Server**:
   ```bash
   npm run dev
   ```

---

## 📁 Repository Directory Structure
*Strict folder mapping conventions.*
```
BrainAI/
├── docs/             # Documentation and templates (Obsidian Vault)
├── src/              # Application source code
│   ├── components/   # Reusable UI components
│   ├── controllers/  # API controllers / route handlers
│   ├── models/       # Database query models
│   ├── routes/       # API router configurations
│   ├── utils/        # Shared helper utilities
│   └── index.js      # Application entrypoint
├── tests/            # Test suites
└── package.json      # Dependencies and scripts
```

---

## 📜 Coding Conventions

### Naming Conventions
- **Files/Folders**: `kebab-case` (e.g., `user-profile.js`, `login-form.css`)
- **JavaScript Classes**: `PascalCase` (e.g., `UserRepository`)
- **JavaScript Functions/Variables**: `camelCase` (e.g., `fetchUserData`)
- **Database Tables/Columns**: `snake_case` (e.g., `created_at`, `user_metadata`)

### Guidelines for AI Developers
1. **Preserve Code Comments**: Do not delete existing comments unless requested.
2. **Modular Functions**: Keep functions focused, small, and pure where possible.
3. **Vanilla CSS Design**: Rely on standard variables and CSS custom properties defined in `index.css`.
4. **No Code Placeholders**: Never write comments like `// implement later`. Write complete, working solutions.

---

## 🌿 Git Workflow & Commit Guidelines

We use **Conventional Commits**:
- `feat(auth): add login endpoint` - New feature
- `fix(db): resolve database connection timeout` - Bug fix
- `docs(readme): update setup instructions` - Documentation change
- `refactor(users): optimize query performance` - Refactoring code

Branch naming convention: `feature/short-desc` or `bugfix/short-desc`.
