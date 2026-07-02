---
project: "PROJECT_NAME"
role: "Architect"
last_updated: 2026-07-02
tags:
  - security
  - owasp
  - guidelines
  - compliance
---

# 🛡️ Secure Coding & OWASP Compliance Guidelines

◀️ Back to [[Project_Hub]] | Architecture: [[system_architecture]]

This document defines the strict security requirements and standards that all generated code must comply with. These rules are modeled after the **OWASP Top 10** and **CWE Top 25** standards.

---

## ❌ Strict AI Security Constraints (Güvenli Kodlama Kuralları)

Any AI Agent modifying this codebase must adhere to the following secure coding patterns. Failure to do so will result in rejected pull requests.

### 1. Injection Prevention (CWE-89, CWE-78)
*   **SQL Injection**: Never concatenate input variables directly into SQL queries. You **must** use parameterized queries (prepared statements) or a trusted ORM.
*   **Command Injection**: Avoid executing system commands (`child_process.exec`, `os.system`) with raw user inputs. If mandatory, sanitize inputs using strict allow-lists.

### 2. Cross-Site Scripting (XSS) Prevention (CWE-79)
*   **UI Rendering**: Never bypass default UI framework escaping (e.g., do not use `dangerouslySetInnerHTML` in React or `innerHTML` in vanilla JS unless absolutely verified and sanitized using a library like DOMPurify).
*   **Reflected/Stored XSS**: Always escape outputs contextually before rendering them in HTML, attributes, or scripts.

### 3. Sensitive Data Protection & Secret Management (CWE-798, CWE-312)
*   **Hardcoded Secrets**: Never hardcode API keys, passwords, private keys, or webhook tokens in code, comments, or configurations. Use environment variables (`.env`).
*   **Logging**: Never log PII (Personally Identifiable Information), passwords, session tokens, or JWT payloads in application console logs.
*   **Passwords**: Passwords must be hashed using a strong, industry-standard cryptographic function (e.g., Argon2id or bcrypt) with an appropriate salt/work factor. Never store plaintext passwords.

### 4. Broken Object Level Authorization (BOLA / IDOR) (CWE-285)
*   **Server-side Verification**: Never rely on frontend state or hidden parameters for access control.
*   **Contextual Checks**: Every API endpoint handling private user data **must** verify that the authenticated session owner (`req.user.id`) matches the owner of the resource being requested.

### 5. Secure Error Handling (CWE-209)
*   **Information Disclosure**: Never return raw database errors, stack traces, or internal server configurations in API responses.
*   **Safe Responses**: Catch errors gracefully and return generic, friendly error messages to clients (e.g., `"An internal error occurred."`) while logging the detailed stack trace to secure server-side logging systems.

---

## 🚦 AI Agent Security Self-Audit Checklist
Before submitting code, the AI developer **must** verify the following:

- [ ] Does this code introduce any database queries? If yes, are prepared statements used?
- [ ] Does this code handle secrets? If yes, are they loaded exclusively via `process.env` (or language equivalent)?
- [ ] Does this code store passwords? If yes, are they hashed with bcrypt/argon2?
- [ ] Does this code accept user input? If yes, is it validated for type, range, and format on the server side?
- [ ] Are API endpoints protected by authorization checks, verifying resource ownership?
- [ ] Have I avoided exposing stack traces in client-facing error messages?
