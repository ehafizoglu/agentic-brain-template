# 🧠 Agentic Brain Framework (ABF)

* 🇹🇷 [Türkçe Kullanım Kılavuzu için buraya tıklayın](README_TR.md)

An enterprise-grade, Obsidian-compatible scaffolding template designed to optimize communication with AI Agents (Claude Code, Cursor, ChatGPT, Claude) while preventing "vibe coding" through disciplined, structured engineering vaults.

---

## 🚀 Quick Start

### Step 1: Clone or Copy
Clone this repository to your local machine:
```bash
git clone https://github.com/ehafizoglu/agentic-brain-template.git my-new-project
cd my-new-project
```

### Step 2: Initialize
Run the bootstrapper script to customize the templates, clean legacy git histories, and set up your new project variables:
```bash
python scripts/init_project.py
```
*This script will ask you for your **Project Name** and **Developer Name**, automatically replace the template placeholders, reset git history, and build your initial AI context.*

### Step 3: Open in Obsidian
Open **Obsidian** and click **"Open folder as vault"**, then select the `docs` directory. This keeps your note interface clean from source code.

---

## 🤖 Feeding Context to Other AIs

If you are using ChatGPT, Claude Web, or another AI chat interface and want to onboard the AI to your project in one step, run the documentation compiler:

```bash
python scripts/bundle_ai_context.py
```

This compiles your global rules, active task lists, requirements, architecture schemas, and testing scenarios into a single file at the root: **`ai_context_merged.md`**. 
Simply drag-and-drop or upload this file into your AI chat window.

---

## 📁 Directory Architecture

```
├── CLAUDE.md                         # Global AI Rules & Commands (Matt Pocock Style)
├── .cursorrules                      # Rule configurations for Cursor/Windsurf
├── docs/                             # Obsidian Documentation Vault
│   ├── 00_Core/
│   │   ├── Project_Hub.md            # Map of Content (MOC) Dashboard
│   │   └── ADRs/                     # Architectural Decision Records ledger
│   ├── 01_Analyst/
│   │   └── business_requirements.md  # Vision, Scope, Features, User Stories
│   ├── 02_Architect/
│   │   ├── system_architecture.md    # Tech Stack, Database (Mermaid), API contracts
│   │   └── security_guidelines.md    # OWASP & CWE secure coding guidelines
│   ├── 03_Developer/
│   │   ├── development_guide.md      # Conventions, setup, folder rules
│   │   └── task_board.md             # Active Kanban task board
│   ├── 04_Tester/
│   │   └── test_plan.md              # Gherkin Test cases, QA strategy, Bug logs
│   └── 05_Memory/
│       ├── lessons_learned.md        # AI memory of resolved bugs, technical quirks
│       └── active_context.md         # Brief status summary for quick prompts
├── scripts/
│   ├── init_project.py               # Project initialization bootstrapper
│   └── bundle_ai_context.py          # AI context compilation script
└── src/                              # Your application source code folder
```

---

## ❌ The Anti-Vibe-Coding Rules

To maintain disciplined software engineering, this template enforces the following cognitive rules inside `CLAUDE.md`:

1.  **The Clarification Phase**: If task requirements are even slightly ambiguous, the AI **must** ask at least 2 clarifying questions before editing any code.
2.  **Test-First Design**: The AI must write or specify testing scenarios under `test_plan.md` before implementing the code.
3.  **No Code Placeholders**: No stub methods, no half-written files, and no `// TODO` comments in place of functional logic.
4.  **Memory Ledger**: Significant bugs, API quirks, and root causes must be logged in `lessons_learned.md` to prevent repetitive loops.
