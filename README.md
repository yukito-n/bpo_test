# BPO Operations Management Tool

This project provides a small internal web application for managing BPO operations on a local network. It uses FastAPI and SQLite and is designed to run entirely without external cloud services.

## Setup

1. Install Python 3.10+ and create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
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

## Updating

Stop the server, replace the source code, and restart the command above. The SQLite database file should be backed up via existing procedures.
