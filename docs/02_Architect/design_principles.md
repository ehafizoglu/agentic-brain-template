---
project: "PROJECT_NAME"
role: "Architect"
last_updated: 2026-07-02
tags:
  - design-principles
  - clean-code
  - architecture
---

# 🎨 Design & Coding Principles Guidelines

◀️ Back to [[Project_Hub]] | Architecture: [[system_architecture]]

This document outlines the software design patterns, coding standards, and architectural layout rules that must be enforced in this project.

---

## 🏗️ 1. Core Coding Philosophy

*   **SOLID Compliance**:
    *   **Single Responsibility Principle (SRP)**: Each module, function, or class must do exactly one thing and have only one reason to change.
    *   **Open/Closed Principle (OCP)**: Code should be open for extension but closed for modification. Use polymorphism or configuration interfaces rather than massive switch/if-else chains.
    *   **Dependency Inversion Principle (DIP)**: High-level modules must not depend on low-level modules; both must depend on abstractions.
*   **DRY (Don't Repeat Yourself)**: Avoid copy-pasting code blocks. Any logic repeated more than twice must be abstracted into a helper utility or service.
*   **KISS (Keep It Simple, Stupid)**: Write simple, readable code over clever or highly nested configurations. Code readability is a priority.
*   **YAGNI (You Aren't Gonna Need It)**: Do not write code or design endpoints for potential future features unless explicitly requested.

---

## 📁 2. Layered Architecture & Separation of Concerns

We enforce a strict separation of concerns. Modules must reside in their designated directories and only communicate with adjacent layers:

```
[Client Request] ──> [Routes / Controllers] ──> [Services / Domain Logic] ──> [Models / Database]
```

### A. Routes & Controllers (`src/routes/`, `src/controllers/`)
- **Responsibility**: Parse HTTP headers/query params, validate request bodies, handle status codes (e.g., 200, 400), and call service methods.
- **Rule**: No business logic calculations and no database queries are allowed inside controllers.

### B. Services (`src/services/`)
- **Responsibility**: Contain all business rules, calculate data operations, handle workflow logic, and trigger third-party API integration.
- **Rule**: Services must not parse raw Express `req` or `res` objects directly. They receive plain inputs and return plain objects.

### C. Models & Repositories (`src/models/`, `src/db/`)
- **Responsibility**: Build database schemas, define data types, write raw/ORM SQL queries, and sanitize database inputs.
- **Rule**: This is the only layer allowed to communicate with the database.
