import subprocess

def get_git_diff() -> str:
    """
    Get the current git diff for the HEAD.
    """
    try:
        if not check_git_status():
            return ""
        
        result = subprocess.run(
            ["git", "diff", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error fetching git diff: {e}")
        return ""

def check_git_status() -> bool:
    """
    Check whether the git is installed and the current directory is a git repository.
    """
    try:
        subprocess.run(["git", "status"], check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError:
        return False