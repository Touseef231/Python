import subprocess
import os
from datetime import datetime

# Your main project folder path
REPO_PATH = r"C:\Python"

def backup_and_push():
    if not os.path.exists(REPO_PATH):
        print(f"Error: Path '{REPO_PATH}' does not exist.")
        return

    try:
        # 1. Stage all changed files (.gitignore, README.md, etc.)
        subprocess.run(["git", "add", "."], cwd=REPO_PATH, check=True)
        
        # Create a timestamp for the commit message
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_message = f"Auto-update: {timestamp}"
        
        # 2. Commit the changes locally
        commit_result = subprocess.run(
            ["git", "commit", "-m", commit_message], 
            cwd=REPO_PATH, 
            capture_output=True, 
            text=True
        )
        
        # Check if there was actually anything new to commit
        if "nothing to commit" in commit_result.stdout or "nothing added to commit" in commit_result.stdout:
            print("No local changes detected. Everything is already saved.")
            return
            
        print("Changes committed locally.")

        # 3. Push the changes to GitHub
        print("Uploading to remote repository...")
        push_result = subprocess.run(
            ["git", "push"], 
            cwd=REPO_PATH, 
            capture_output=True, 
            text=True, 
            check=True
        )
        
        print("\nSuccess! Your repository has been updated online.")
        
    except subprocess.CalledProcessError as e:
        print("\nGit operation failed. Error details:")
        print(e.stderr if e.stderr else e.stdout)

if __name__ == "__main__":
    backup_and_push()
    input("\nPress Enter to close this window...")
