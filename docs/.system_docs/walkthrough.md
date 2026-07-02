# Walkthrough: Multi-Role Agentic Brain Framework (ABF) Integration

I have successfully expanded the **Agentic Brain Framework (ABF)** inside your project directory into a complete **Multi-Role Virtual Organization Workspace**. This environment now supports specialized AI agents for **Product Management**, **UI/UX Design**, and **DevOps Engineering**, alongside Developers, Testers, and Architects.

---

## 🛠️ Upgraded Directory & Rule Architecture

Here is the finalized layout of the workspace at `d:\Ozel\Projeler\BrainAI`:

* **`CLAUDE.md`** & **`.cursorrules`**:
  * [CLAUDE.md](file:///d:/Ozel/Projeler/BrainAI/CLAUDE.md) / [.cursorrules](file:///d:/Ozel/Projeler/BrainAI/.cursorrules): Contains the global rulebook, commands, and **Anti-Vibe-Coding protocol** now expanded to 10 rules.
* **`docs/00_Core/`**:
  * [Project_Hub.md](file:///d:/Ozel/Projeler/BrainAI/docs/00_Core/Project_Hub.md): Vault index (MOC) connecting the entire framework.
  * **`ADRs/`**: 
    * [ADR-000-Template.md](file:///d:/Ozel/Projeler/BrainAI/docs/00_Core/ADRs/ADR-000-Template.md): Architectural Decision Record template.
* **`docs/06_Product_Manager/`**:
  * [product_strategy.md](file:///d:/Ozel/Projeler/BrainAI/docs/06_Product_Manager/product_strategy.md): PM strategy templates (target segments, UVP, competitor analysis).
  * [product_roadmap.md](file:///d:/Ozel/Projeler/BrainAI/docs/06_Product_Manager/product_roadmap.md): Strategic milestones, release checklists, and KPIs.
* **`docs/07_DevOps/`**:
  * [deployment_guide.md](file:///d:/Ozel/Projeler/BrainAI/docs/07_DevOps/deployment_guide.md): Environment configs, Docker configuration, and CI/CD validation.
* **`docs/08_UI_UX/`**:
  * [design_system.md](file:///d:/Ozel/Projeler/BrainAI/docs/08_UI_UX/design_system.md): Layout tokens, HSL colors, typography scales, and CSS micro-animation templates.
* **`docs/05_Memory/`**:
  * [lessons_learned.md](file:///d:/Ozel/Projeler/BrainAI/docs/05_Memory/lessons_learned.md): Long-term memory bank.
  * [active_context.md](file:///d:/Ozel/Projeler/BrainAI/docs/05_Memory/active_context.md): Short-term memory card.

---

## 🚀 How the System Prompt Pre-Prompter Works

The upgraded [bundle_ai_context.py](file:///d:/Ozel/Projeler/BrainAI/scripts/bundle_ai_context.py) script has been executed and generates [ai_context_merged.md](file:///d:/Ozel/Projeler/BrainAI/ai_context_merged.md).

When compiled, the script creates a specialized **Pre-Prompt Instruction Wrapper** at the very beginning of the merged file:
1. **Instructs the Target AI**: *"You are an elite, full-stack software engineer, QA lead, and system architect..."*
2. **Injects CLAUDE.md Rules**: Placed right at the top inside markdown fences, forcing the receiving AI to digest your code formatting, TDD, Product, UI/UX, and DevOps rules before reading files.
3. **Parses the Task Board**: Automatically scans `task_board.md` to see what is marked as **In Progress**, highlighting it under `CURRENT WORKSPACE TARGETS` so the AI knows exactly what task it needs to work on.
4. **Appends Vault Files**: Integrates all Analyst, Architect, Developer, Tester, Product, DevOps, UI/UX, and Memory files in alphabetical sequence separated by clean labels.

---

## 🔬 Execution Verification

- **Command Run**: `python scripts/bundle_ai_context.py`
- **Output File**: `d:\Ozel\Projeler\BrainAI\ai_context_merged.md` (949 lines, 31.8 KB)
- **Status**: Successfully compiled. Character encoding issues are fully resolved. Emojis and other Unicode structures render cleanly as UTF-8.
