import sys
from pathlib import Path

def init_notebook_environment():
    """
    Zorg dat de /src map beschikbaar is voor imports.
    """
    SRC_DIR = Path.cwd().parent / "src"
    if SRC_DIR.exists() and str(SRC_DIR) not in sys.path:
        sys.path.insert(0, str(SRC_DIR))
        print(f"✅ SRC toegevoegd aan sys.path: {SRC_DIR}")
    else:
        print(f"ℹ️ SRC al aanwezig of niet gevonden: {SRC_DIR}")
