from fastapi import FastAPI

app = FastAPI(title="My First Python Web App")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from FastAPI!"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
