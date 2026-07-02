# Walkthrough: Agentic Brain Framework (ABF) Integration

I have successfully constructed the **Agentic Brain Framework (ABF)** inside your project directory. This environment enforces professional engineering rules (preventing "vibe coding") and gives any target AI agent an immediate cognitive roadmap and context-awareness.

---

## 🛠️ Upgraded Directory & Rule Architecture

Here is the finalized layout of the workspace at `d:\Ozel\Projeler\BrainAI`:

* **`CLAUDE.md`** & **`.cursorrules`**:
  * [CLAUDE.md](file:///d:/Ozel/Projeler/BrainAI/CLAUDE.md) / [.cursorrules](file:///d:/Ozel/Projeler/BrainAI/.cursorrules): Contains the global rulebook, commands, and **Anti-Vibe-Coding protocol** (forcing the AI to clarify instruction ambiguity, map out tests first, and avoid stubbing/placeholders).
* **`docs/00_Core/`**:
  * [Project_Hub.md](file:///d:/Ozel/Projeler/BrainAI/docs/00_Core/Project_Hub.md): Vault index (MOC) connecting the entire framework.
  * **`ADRs/`**: 
    * [ADR-000-Template.md](file:///d:/Ozel/Projeler/BrainAI/docs/00_Core/ADRs/ADR-000-Template.md): Architectural Decision Record template for saving architectural choices.
* **`docs/05_Memory/`**:
  * [lessons_learned.md](file:///d:/Ozel/Projeler/BrainAI/docs/05_Memory/lessons_learned.md): Long-term memory log. Houses platform quirks, resolved bug writeups, and refactoring notes.
  * [active_context.md](file:///d:/Ozel/Projeler/BrainAI/docs/05_Memory/active_context.md): Short-term memory card summarizing current sprints and priorities for small-window prompts.

---

## 🚀 How the System Prompt Pre-Prompter Works

The upgraded [bundle_ai_context.py](file:///d:/Ozel/Projeler/BrainAI/scripts/bundle_ai_context.py) script has been executed and generates [ai_context_merged.md](file:///d:/Ozel/Projeler/BrainAI/ai_context_merged.md).

When compiled, the script creates a specialized **Pre-Prompt Instruction Wrapper** at the very beginning of the merged file:
1. **Instructs the Target AI**: *"You are an elite, full-stack software engineer, QA lead, and system architect..."*
2. **Injects CLAUDE.md Rules**: Placed right at the top inside markdown fences, forcing the receiving AI to digest your code formatting and TDD rules before reading files.
3. **Parses the Task Board**: Automatically scans `task_board.md` to see what is marked as **In Progress**, highlighting it under `CURRENT WORKSPACE TARGETS` so the AI knows exactly what task it needs to work on.
4. **Appends Vault Files**: Integrates all Analyst, Architect, Developer, Tester, and Memory files in alphabetical sequence separated by clean labels.

---

## 🔬 Execution Verification

- **Command Run**: `python scripts/bundle_ai_context.py`
- **Output File**: `d:\Ozel\Projeler\BrainAI\ai_context_merged.md` (648 lines, 22.2 KB)
- **Status**: Successfully compiled. Character encoding issues (such as `ğŸ¤–` and `âš ï¸`) are fully resolved. Emojis and other Unicode structures render cleanly as UTF-8.
