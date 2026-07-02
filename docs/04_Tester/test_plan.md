---
project: "PROJECT_NAME"
role: "Tester"
last_updated: 2026-07-02
tags:
  - role/tester
  - test-plan
  - qa
---

# 🧪 Tester: Quality Assurance & Verification Plan

◀️ Back to [[00_Project_Hub]] | Requirements: [[business_requirements]]

This document outlines the testing strategy, active test cases, acceptance criteria verification, and bug logs.

---

## 🎯 QA Strategy & Tools
We enforce a robust quality pipeline utilizing the following methodologies:
- **Unit Testing**: Jest / Vitest (aiming for >80% coverage)
- **Integration Testing**: Supertest (testing API endpoints in isolation)
- **End-to-End Testing**: Playwright (verifying critical user paths)

---

## 🎭 Test Scenarios & Acceptance Criteria (Gherkin Style)
*Write test cases using Gherkin syntax (Given-When-Then). AI agents can parse this to write automated tests instantly.*

### 🧪 TC-001: Success Login
- **Feature**: User Login
- **Scenario**: A user successfully logs in with valid credentials
  - **Given** the user is on the login page `/login`
  - **When** the user enters a registered email `"user@example.com"`
  - **And** enters the correct password `"securepassword123"`
  - **And** clicks the "Login" button
  - **Then** the system should issue a session token
  - **And** redirect the user to the dashboard page `/dashboard`

### 🧪 TC-002: Failed Login (Invalid Password)
- **Feature**: User Login
- **Scenario**: A user fails to log in due to incorrect credentials
  - **Given** the user is on the login page `/login`
  - **When** the user enters a registered email `"user@example.com"`
  - **And** enters an incorrect password `"wrongpassword"`
  - **And** clicks the "Login" button
  - **Then** the login page should display an error message `"Invalid email or password"`
  - **And** the user should remain on the `/login` page

---

## 🐛 Active Bug Log
*Log any issues identified during manual or automated testing.*

| Bug ID | Description | Severity | Steps to Reproduce | Status |
| :--- | :--- | :--- | :--- | :--- |
| **BUG-001** | Login page does not load in Safari | `Medium` | 1. Open Safari<br>2. Visit `/login`<br>3. Blank screen | `🔴 Open` |
| **BUG-002** | Form button doesn't show loading spinner | `Low` | 1. Click login<br>2. Button is disabled but static | `🟢 Resolved` |
