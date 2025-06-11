import os

# Determine the project root so the default path is stable no matter where
# Uvicorn is launched from.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Location of the SQLite database file. Users can override this with the
# BPO_DB_PATH environment variable to point at a shared network drive.
DB_PATH = os.getenv("BPO_DB_PATH", os.path.join(PROJECT_ROOT, "bpo_tool.db"))

DATABASE_URL = f"sqlite:///{DB_PATH}"
