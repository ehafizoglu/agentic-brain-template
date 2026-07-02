import os
import re
from datetime import datetime

output_file = "ai_context_merged.md"
docs_dir = "docs"
claude_file = "CLAUDE.md"

print("========================================================")
print("  Advanced Documentation Compiler for AI Agents (ABF)   ")
print("========================================================")

# 1. Read CLAUDE.md rules
claude_rules = ""
if os.path.exists(claude_file):
    print("Found CLAUDE.md system rules. Injecting into AI pre-prompt...")
    with open(claude_file, "r", encoding="utf-8") as f:
        claude_rules = f.read()

# 2. Try to parse active tasks from task_board.md
active_tasks = "No active tasks specified."
task_board_path = os.path.join(docs_dir, "03_Developer", "task_board.md")
if os.path.exists(task_board_path):
    with open(task_board_path, "r", encoding="utf-8") as f:
        board_content = f.read()
    # Find In Progress section
    match = re.search(r"### 🔄 In Progress.*?(###|$)", board_content, re.DOTALL)
    if match:
        tasks = re.findall(r"-\s*\[\s*\].*", match.group(0))
        if tasks:
            active_tasks = "\n".join(t.strip() for t in tasks)

# 3. Create the Advanced AI Pre-Prompt Header
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
header = f"""# 🤖 COMPILED PROJECT CONTEXT & AI INSTRUCTIONS

> **System Instruction**: You are an elite, full-stack software engineer, QA lead, and system architect. 
> You have been provided with the complete consolidated context of the project.
> Read the global rules below and immediately adapt your behavior to match them.

---

## ⚠️ SYSTEM INSTRUCTIONS & COGNITIVE RULES
These rules govern how you write code, ask questions, and design systems for this project.

```markdown
{claude_rules}
```

---

## 📋 CURRENT WORKSPACE TARGETS
**Current Active Tasks (From Task Board):**
{active_tasks}

**Generated on:** {timestamp}

---
"""

with open(output_file, "w", encoding="utf-8") as out:
    out.write(header)
    
    # 4. Gather and sort all markdown files
    md_files = []
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md") and file != output_file:
                full_path = os.path.join(root, file)
                md_files.append(full_path)
                
    # Sort files alphabetically to ensure consistent structure
    md_files.sort()
    
    for file_path in md_files:
        rel_path = os.path.relpath(file_path, start=".").replace("\\", "/")
        print(f"Processing: {rel_path}")
        
        separator = f"\n\n# ================================================================================\n# FILE: {rel_path}\n# ================================================================================\n\n"
        out.write(separator)
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        out.write(content)

print("========================================================")
print(f"Success! Created compiled context at: {output_file}")
print("========================================================")
