import os
import sys
import subprocess

# Get absolute path to this script's directory (the project root)
project_root = os.path.dirname(os.path.abspath(__file__))

# Activate virtual environment if not already active
if os.name == "nt" or sys.platform == "win32":
    venv_python = os.path.join(project_root, ".venv", "Scripts", "python.exe")
else:
    venv_python = os.path.join(project_root, ".venv", "bin", "python")
if os.path.exists(venv_python) and sys.executable.lower() != venv_python.lower():
    # Relaunch this script using the venv's python
    subprocess.run([venv_python, __file__] + sys.argv[1:])
    sys.exit(0)

# Launch Uvicorn using the correct module path
try:
    subprocess.run([
        sys.executable, "-m", "uvicorn", "api.app:app", "--reload"
    ])
except Exception as e:
    print("Failed to launch Uvicorn:", e)
    sys.exit(1)
