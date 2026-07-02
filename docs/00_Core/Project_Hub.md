---
project: "PROJECT_NAME"
version: "1.0.0"
status: "Planning" # Planning, Active, Paused, Completed
owner: "USER_NAME"
last_updated: 2026-07-02
tags:
  - project-hub
  - status/planning
---

# 📑 Project Hub: PROJECT_NAME

Welcome to the central command hub of **PROJECT_NAME**. This workspace is structured to be atomic, modular, and optimized for both **Obsidian** and **AI Agents**.

---

## 🎯 Executive Summary
> [!NOTE]
> *Provide a brief 2-3 sentence overview of what this project is, who it is for, and the primary problem it solves.*

---

## 🗺️ Project Map (Role-Based Views)

| Role | Key Document | Description | Status |
| :--- | :--- | :--- | :--- |
| **🕵️ Analyst** | [[business_requirements]] | Scope, goals, user stories, Moscow priorities | `🔴 Not Started` |
| **📐 Architect** | [[system_architecture]] | Tech stack, database schemas (Mermaid), APIs | `🔴 Not Started` |
| **💻 Developer** | [[development_guide]] | Setup, naming rules, folder conventions | `🔴 Not Started` |
| **📋 Developer Board** | [[task_board]] | Active task board / Kanban checklist | `🔴 Not Started` |
| **🧪 Tester** | [[test_plan]] | QA strategy, Gherkin scenarios, bug logs | `🔴 Not Started` |

---

## 🧠 Brain Vault & ADR Ledger

*   **Architectural Decisions**: [[ADR-000-Template]] – Log of technical decisions.
*   **Memory Bank**: [[lessons_learned]] – Root causes of bugs, fixes, and lessons learned.
*   **Active Context**: [[active_context]] – A short summary of the current state of work.

---

## 🤖 AI Integration Guide (Read Me)
To feed this entire project to another AI in one single action:
1. Run the compilation script from your terminal:
   ```bash
   python scripts/bundle_ai_context.py
   ```
2. This creates `ai_context_merged.md` at the project root.
3. Drag-and-drop or upload `ai_context_merged.md` into the target AI chat. It will instantly understand your entire project architecture, requirements, and codebase status.
