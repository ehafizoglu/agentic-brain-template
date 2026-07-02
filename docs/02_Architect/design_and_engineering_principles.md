---
project: "PROJECT_NAME"
role: "Architect"
last_updated: 2026-07-02
tags:
  - design-principles
  - error-handling
  - logging
  - performance
---

# 📐 Design & Engineering Principles Guidelines

◀️ Back to [[Project_Hub]] | Architecture: [[system_architecture]]

This document outlines the software engineering principles, error-handling conventions, logging standards, and performance patterns that must be enforced in this project.

---

## 🎨 1. Design & Coding Principles (Tasarım Prensipleri)
To keep the codebase maintainable and scalable, the AI agent must enforce:

*   **SOLID Compliance**:
    *   *Single Responsibility*: Each module/class must have only one reason to change.
    *   *Dependency Inversion*: Code against abstractions (interfaces), not concrete implementations.
*   **DRY & KISS**: Never copy-paste logic; refactor into shared utils. Keep algorithms simple and self-documenting.
*   **Layered Architecture Separation**: Strictly isolate application layers:
    *   `Routes / Controllers`: Parse requests, validate payloads, call services. No database queries.
    *   `Services / Business Logic`: Handle domain logic, calculations, third-party APIs.
    *   `Models / Repositories`: Interface directly with the database.

---

## 🛑 2. Standardized Error Handling (Hata Yönetimi)
We enforce a robust, centralized exception handling strategy:

*   **Custom AppError Class**: Use a unified error class inheriting from `Error` that includes HTTP status codes and operational flags.
*   **No Unhandled Promises**: Always wrap async operations in try/catch or use an async boundary wrapper for controller routes.
*   **Centralized Middleware**: Catch all errors in a global error handler.
    *   *Non-Operational Errors*: Log details with high severity and restart the process if necessary (process crashing on uncaught exceptions).
    *   *Operational Errors*: Return structured client payloads:
        ```json
        {
          "success": false,
          "error": {
            "code": "VALIDATION_FAILED",
            "message": "The request payload is invalid."
          }
        }
        ```

---

## 🪵 3. Logging & Observability (Loglama ve İzlenebilirlik)
*   **Structured Logging**: Use JSON logging in production (using libraries like Winston or Pino) for easy parsing by monitoring systems (ELK, Datadog).
*   **Trace/Correlation IDs**: Attach a unique request UUID (`trace-id`) to every request session. This ID must be injected in all logs generated during that request pipeline to allow quick debugging.
*   **Log Levels**: Enforce appropriate levels:
    *   `FATAL`: System crash, process must stop.
    *   `ERROR`: Operational failures (database down, email dispatch failed).
    *   `WARN`: Unusual behavior, not a failure (rate limit hit, validation warning).
    *   `INFO`: High-level operations (user logged in, server started).
    *   `DEBUG`: Highly verbose logs for local troubleshooting (payload logs).

---

## ⚡ 4. Performance & DB Best Practices (Performans)
*   **Avoid N+1 Query Problems**: Always batch-load or join related records instead of querying the database inside loops.
*   **Database Indexing**: Any column queried in `WHERE`, `JOIN`, or `ORDER BY` operations must have an appropriate index designed in the schema.
*   **Paginated APIs**: List/Search APIs must enforce limit/offset or cursor-based pagination. Returning unbounded rows is strictly forbidden.
*   **Caching Policy**: Cache expensive, slow-changing database queries or computation results using Redis. Establish clear cache invalidation policies (TTL).
