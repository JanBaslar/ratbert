import os
import pathlib
import subprocess
import sys
import venv


VENV_DIR = "venv"
REQUIREMENTS_FILE = "requirements.txt"
APP_MAIN_FILE = "src/main.py"


def _verify_environment() -> None:
    """Verifies correct location and Python version."""
    if pathlib.Path.cwd().name != "ratbert" or not os.path.exists(APP_MAIN_FILE):
        print("Error: Correct environment not detected. Please run this script from the root 'ratbert' directory.")
        sys.exit(1)

    if sys.version_info < (3, 9):
        print("Error: Python 3.9 or higher is required.")
        sys.exit(1)


def _create_venv_if_not_exists() -> None:
    """Creates a virtual environment if it doesn't already exist."""
    if not os.path.exists(VENV_DIR):
        print("First-time setup: Creating Python virtual environment...")
        venv.create(VENV_DIR, with_pip=True)


def _get_venv_python() -> str:
    """Returns the correct path to the virtual environment's Python executable."""
    # 'nt' for Windows
    if os.name == 'nt':
        return os.path.join(VENV_DIR, "Scripts", "python.exe")
    else:
        return os.path.join(VENV_DIR, "bin", "python")


def _install_required_libraries(venv_python: str) -> None:
    """Installs required libraries from requirements.txt using the virtual environment's pip."""
    doLogInstall = True if sys.argv[-1] == "-v" else False
    if os.path.exists(REQUIREMENTS_FILE):
            print("Installing required libraries...")
            subprocess.check_call([venv_python, "-m", "pip", "install", "-r", REQUIREMENTS_FILE], 
                                  stdout=subprocess.DEVNULL if not doLogInstall else None,
                                  stderr=subprocess.DEVNULL if not doLogInstall else None)
    else:
        print(f"WARNING: {REQUIREMENTS_FILE} not found. Skipping installs...")


def _launch_app(venv_python: str) -> None:
    """Launches the main application using the virtual environment's Python executable."""
    print("Launching RATBERT...")
    try:
        subprocess.check_call([venv_python, APP_MAIN_FILE])
    except KeyboardInterrupt:
        print("App closed")


def setup_and_run() -> None:
    """Sets up the environment and runs the application."""
    _verify_environment()
    _create_venv_if_not_exists()
    venv_python = _get_venv_python()
    _install_required_libraries(venv_python)
    _launch_app(venv_python)


if __name__ == "__main__":
    setup_and_run()
