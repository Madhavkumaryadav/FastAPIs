# FastAPI Basics (Learning Series)

This folder contains the beginner FastAPI example.

## File

- `fastapi_01.py`

## What This App Covers

- Creating a FastAPI app
- Defining basic `GET` endpoints
- Returning JSON responses

## Run This App

From the project root (`FastAPIs`):

```bash
uvicorn fastapi.fastapi_01:app --reload
```

Or from inside this folder (`fastapi`):

```bash
uvicorn fastapi_01:app --reload
```

## Endpoints

1. `GET /`
   Returns a welcome message.

2. `GET /about`
   Returns a short about message.

## API Docs

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
