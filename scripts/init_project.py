import os
import shutil
import subprocess

def get_input(prompt, default=""):
    val = input(f"{prompt} [{default}]: ").strip()
    return val if val else default

def main():
    print("========================================================")
    print("  🚀 Agentic Brain Framework (ABF) Project Bootstrapper ")
    print("========================================================")

    # 1. Gather project variables
    project_name = get_input("Enter the new project name", "MyNewProject")
    owner_name = get_input("Enter owner/developer name", "Developer")

    # 2. Files to process
    files_to_update = [
        "CLAUDE.md",
        ".cursorrules",
        "README.md",
        "README_TR.md",
        "docs/00_Core/Project_Hub.md",
        "docs/00_Core/SOUL.md",
        "docs/01_Analyst/business_requirements.md",
        "docs/01_Analyst/office_hours.md",
        "docs/02_Architect/system_architecture.md",
        "docs/02_Architect/security_guidelines.md",
        "docs/02_Architect/design_principles.md",
        "docs/02_Architect/engineering_principles.md",
        "docs/03_Developer/development_guide.md",
        "docs/03_Developer/task_board.md",
        "docs/04_Tester/test_plan.md",
        "docs/05_Memory/lessons_learned.md",
        "docs/05_Memory/active_context.md",
        "docs/06_Product_Manager/product_strategy.md",
        "docs/06_Product_Manager/product_roadmap.md",
        "docs/07_DevOps/deployment_guide.md",
        "docs/08_UI_UX/design_system.md",
        "docs/.system_docs/walkthrough.md",
        "scripts/bundle_ai_context.py"
    ]

    print("\nReplacing placeholder variables in templates...")
    for file_path in files_to_update:
        if os.path.exists(file_path):
            print(f"  Updating: {file_path}")
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Replace variables
            content = content.replace("PROJECT_NAME", project_name)
            content = content.replace("USER_NAME", owner_name)
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

    # 3. Clean up compiled files
    merged_file = "ai_context_merged.md"
    if os.path.exists(merged_file):
        print(f"\nCleaning legacy compiled file: {merged_file}")
        os.remove(merged_file)

    # 4. Optional Git Re-initialization
    git_dir = ".git"
    if os.path.exists(git_dir):
        choice = get_input("\nReset Git history and start a fresh repository for this project? (y/n)", "y").lower()
        if choice in ['y', 'yes']:
            print("Resetting Git history...")
            try:
                # Remove read-only files if necessary (common on Windows)
                def remove_readonly(func, path, excinfo):
                    os.chmod(path, 0o777)
                    func(path)
                shutil.rmtree(git_dir, onerror=remove_readonly)
                
                # Re-initialize git
                subprocess.run(["git", "init"], check=True)
                subprocess.run(["git", "add", "."], check=True)
                subprocess.run(["git", "commit", "-m", "chore: init fresh codebase from Agentic Brain Framework template"], check=True)
                print("  Success: Fresh Git repository initialized!")
            except Exception as e:
                print(f"  Warning: Could not fully reset Git history: {e}")

    # 5. Run compiler to generate fresh context
    print("\nRunning compiler to build initial AI context...")
    try:
        subprocess.run(["python", "scripts/bundle_ai_context.py"], check=True)
    except Exception as e:
        print(f"  Warning: Could not run compiler: {e}")

    print("\n========================================================")
    print(f" 🎉 Project '{project_name}' successfully initialized!")
    print(" You are ready to start coding with your AI agent.")
    print("========================================================")

if __name__ == "__main__":
    main()
