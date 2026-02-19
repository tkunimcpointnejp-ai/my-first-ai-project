# Python Web App (FastAPI)

## Setup

```bash
cd python_web_app
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

Open: http://127.0.0.1:8000

## Endpoints

- `GET /`
- `GET /health`

## Test

```bash
pytest -q
```
