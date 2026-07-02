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
| **🧠 Ideation & Think** | [[office_hours]] | Brainstorming sessions, trade-offs, edge cases | `🔴 Not Started` |
| **🎯 Product** | [[product_strategy]] | Competitor matrices, product market fit, KPIs | `🔴 Not Started` |
| **🗺️ Roadmap** | [[product_roadmap]] | Strategic milestone roadmap & release gates | `🔴 Not Started` |
| **🕵️ Analyst** | [[business_requirements]] | Scope, goals, user stories, Moscow priorities | `🔴 Not Started` |
| **📐 Architect** | [[system_architecture]] | Tech stack, database schemas (Mermaid), APIs | `🔴 Not Started` |
| **💻 Developer** | [[development_guide]] | Setup, naming rules, folder conventions | `🔴 Not Started` |
| **📋 Developer Board** | [[task_board]] | Active task board / Kanban checklist | `🔴 Not Started` |
| **🧪 Tester** | [[test_plan]] | QA strategy, Gherkin scenarios, bug logs | `🔴 Not Started` |
| **🎨 UI/UX Design** | [[design_system]] | Layout tokens, colors, typography, styles | `🔴 Not Started` |
| **⚙️ DevOps** | [[deployment_guide]] | Environments, Docker setup, CI/CD pipelines | `🔴 Not Started` |

---

## 🧠 Brain Vault & ADR Ledger

*   **Architectural Decisions**: [[ADR-000-Template]] – Log of technical decisions.
*   **AI Agent Persona (SOUL)**: [[SOUL]] – Cognitive constitution, behavioral blueprints, and ethical guardrails.
*   **Office Hours Ledger**: [[office_hours]] – Brainstorming logs and technology trade-off evaluations.
*   **Secure Coding Guidelines**: [[security_guidelines]] – OWASP & CWE secure coding compliance rules.
*   **Design Principles**: [[design_principles]] – SOLID, DRY/KISS, and layered architecture conventions.
*   **Engineering & System Principles**: [[engineering_principles]] – Standards for error handling, structured logging, database scaling, and caching.
*   **Memory Bank**: [[lessons_learned]] – Root causes of bugs, fixes, and lessons learned.
*   **Active Context**: [[active_context]] – A short summary of the current state of work.

---

## 🤖 AI Integration & Scaffolding Guide

### 🚀 Starting a New Project (Yeni Proje Başlatma)
Eğer bu klasörü başka bir projede şablon olarak kopyaladıysanız, yeni projeyi otomatik yapılandırmak için terminalinizde şu komutu çalıştırın:
```bash
python scripts/init_project.py
```
*Bu betik; proje adını ve geliştirici ismini şablonlardaki yerlerine otomatik olarak yazar, eski git geçmişini temizler ve ilk derlemeyi tetikler.*

### 📦 Başka Bir Yapay Zekaya Aktarma (Tek Kalemde)
Yapay zekanın tüm dökümantasyonu tek seferde okumasını sağlamak için:
1. Derleme betiğini çalıştırın:
   ```bash
   python scripts/bundle_ai_context.py
   ```
2. Oluşan `ai_context_merged.md` dosyasını hedef AI chat ekranına sürükleyip bırakın. Birleştirilmiş dosya, kural setlerini en tepede barındırarak yapay zekayı doğrudan eğitir.
