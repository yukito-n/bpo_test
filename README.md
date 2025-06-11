# BPO Operations Management Tool

This project provides a small internal web application for managing BPO operations on a local network. It uses FastAPI and SQLite and is designed to run entirely without external cloud services.

## Setup

1. Install Python 3.10+ and create a virtual environment:

```bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install "fastapi[all]" sqlalchemy
```

3. Configure the path to the shared network drive by setting the `BPO_DB_PATH` environment variable or editing `app/config.py`.

4. Initialize the database (automatically done on first run) or run manually:

```bash
python -m app.init_db
```

5. Start the server PC with:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The `--host 0.0.0.0` option listens on all network interfaces. You should **not**
replace it with the server's IP address; specifying an address that does not
belong to the machine will cause a "could not bind" error. Once the server is
running, determine the PC's actual IP address (e.g. using `ipconfig` or `ip a`)
and have users navigate to `http://<SERVER_IP>:8000` in their browser.

### Troubleshooting access

If users cannot reach the site:
1. Make sure the server is started from this project directory so templates are found.
2. Verify the firewall on the server PC allows incoming connections on the chosen port (default 8000).
3. Confirm the client PCs are using the correct server IP address obtained via `ipconfig` (Windows) or `ip a` (Linux/Mac).
4. If another service already uses port 8000, run Uvicorn with a different `--port` and update the URL accordingly.

## Updating

Stop the server, replace the source code, and restart the command above. The SQLite database file should be backed up via existing procedures.
