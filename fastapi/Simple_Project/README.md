# Simple_Project: Patients Management API

This folder contains a small FastAPI project that reads patient data from a JSON file.

## Files

- `main.py`
- `paitents.json`

## What This App Covers

- Loading data from JSON
- Serving full data through API endpoints
- Structuring a simple project in FastAPI

## Run This App

From inside this folder (`fastapi/Simple_Project`):

```bash
uvicorn main:app --reload
```

## Endpoints

1. `GET /`
   Returns welcome message for Patients Management API.

2. `GET /view`
   Returns all patient records from `paitents.json`.

## API Docs

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Note

- The filename is `paitents.json` and `main.py` uses the same spelling.
- For correct file loading, run this app from the same folder as `main.py`.
