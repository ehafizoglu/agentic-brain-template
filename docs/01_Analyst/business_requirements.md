---
project: "PROJECT_NAME"
role: "Analyst"
last_updated: 2026-07-02
tags:
  - role/analyst
  - requirements
---

# 🕵️ Analyst: Business & Functional Requirements

◀️ Back to [[00_Project_Hub]]

This document defines the product scope, business rules, prioritization, and user stories. It acts as the source of truth for features and behavior.

---

## 🎯 Vision & Business Goals
*What are we building, why are we building it, and how do we measure success?*
- **Primary Goal**: 
- **Target Audience**: 
- **Success Metrics**: 

---

## 🔍 Project Scope

### ✅ In-Scope (Ne Yapılacak?)
- [ ] Feature 1...
- [ ] Feature 2...
- [ ] Feature 3...

### ❌ Out-of-Scope (Ne Yapılmayacak?)
- [ ] Features reserved for future phases...
- [ ] Legacy browser support...

---

## 📊 Feature Prioritization (MoSCoW)

```yaml
Must Have:
  - Critical features without which the product cannot launch (e.g., User Authentication).
Should Have:
  - Important but not vital features (e.g., Password Reset, Email Notifications).
Could Have:
  - Nice-to-have features that will improve experience if time permits (e.g., Dark Mode, Profile Customization).
Won't Have (this phase):
  - Out of scope items deferred for later releases (e.g., Mobile Apps, Subscriptions).
```

---

## 👤 User Personas
*Describe the users of the system.*
1. **Persona A (e.g., Customer)**: Needs to...
2. **Persona B (e.g., Admin)**: Needs to...

---

## 📖 User Stories & Functional Specs
*Write these in standard user story format (`As a... I want to... So that...`) and add acceptance criteria. AI can directly convert these into test cases.*

### 🛠️ US-1: User Login
- **As a** Registered User
- **I want to** log into the application using my email and password
- **So that** I can access my private dashboard.
- **Acceptance Criteria (Acceptance Checklist)**:
  - [ ] Input validation for email format.
  - [ ] Error message displayed on incorrect credentials.
  - [ ] Token stored securely on successful login and redirects to `/dashboard`.

### 🛠️ US-2: [Feature Name]
- **As a** ...
- **I want to** ...
- **So that** ...
- **Acceptance Criteria**:
  - [ ] ...
