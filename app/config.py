import os

DB_PATH = os.getenv('BPO_DB_PATH', os.path.join(os.getcwd(), 'bpo_tool.db'))
DATABASE_URL = f"sqlite:///{DB_PATH}"
