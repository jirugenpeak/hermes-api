# hermes-api

A simple todo backend built to learn how REST APIs work.

## Setup and run

Tested with Python **3.9.6** on macOS. Other Python versions have not been
verified. You also need Git and curl for the commands below. SQLite support
comes with Python; no separate database server is needed.

```bash
git clone https://github.com/jirugenpeak/hermes-api.git
cd hermes-api
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python __init__.py
python app.py
```

The activation command above is for macOS/Linux shells. On Windows PowerShell,
use `.venv\Scripts\Activate.ps1` instead.

Keep the server running. In a second terminal, check:

```bash
curl -i http://127.0.0.1:5000/health/
curl -i http://127.0.0.1:5000/tasks/
```

Both should return HTTP `200`. Health returns `{"status": "ok"}`; a fresh
database returns `{"tasks": []}`. JSON whitespace may differ.

To try a complete task lifecycle (use an unused ID if you already have tasks):

```bash
curl -i -X POST http://127.0.0.1:5000/tasks/ \
  -H 'Content-Type: application/json' -d '{"id":"1","title":"fix earth"}'
curl -i http://127.0.0.1:5000/tasks/
curl -i -X PUT http://127.0.0.1:5000/tasks/ \
  -H 'Content-Type: application/json' -d '{"id":"1","status":"CLOSED"}'
curl -i http://127.0.0.1:5000/tasks/
curl -i -X DELETE http://127.0.0.1:5000/tasks/ \
  -H 'Content-Type: application/json' -d '{"id":"1"}'
curl -i http://127.0.0.1:5000/tasks/
```

Currently, write operations return the JSON number `200`. Task listings contain
arrays in the order `[id, title, status]`. After creation, task `1` is `OPEN`;
after the PUT it is `CLOSED`; after deletion the list is empty again.

Stop the development server with Ctrl+C. Debug mode is for local development.

## Dependencies and database

The application imports two third-party packages: `flask` (installed as `Flask`)
and `flask_restful` (installed as `Flask-RESTful`). `requirements.txt` pins these
and their transitive dependencies to the versions used in development. `sqlite3`
and `pathlib` are part of Python's standard library.

Run `python __init__.py` before starting the server for the first time. It creates
`hermes.db` beside `todos.py`, regardless of the current working directory.
The server uses the same path. The database is local and ignored by Git.

Running initialization again preserves existing tasks. It creates the table only
if missing; it does not migrate an existing table's schema. The server does not
initialize the database automatically. To start over, stop the server, remove
`hermes.db` (this deletes all tasks), then run initialization again.

To check reproducibility, repeat setup in a separate checkout with a new virtual
environment and no `hermes.db`. Do not copy your existing environment or database.

## What we will build

- Register users and log in.
- Use JWTs to authenticate API requests.
- Create, view, update, and delete tasks.
- Allow users to access only their own tasks.
- Store users and tasks in a database.
- Add pagination and filtering when listing tasks.
- Validate inputs and return clear errors with HTTP status codes.
- Test the API with successful and failed requests.

## How we will use it

We will use a terminal user interface (TUI) instead of a graphical interface. The TUI will send HTTP requests to the backend API. We will not build a web frontend.

The backend will handle authentication, permissions, task management, and database access.

## Name

Hermes is the messenger of the Greek gods. The name fits a project about communication between a client and a server.
