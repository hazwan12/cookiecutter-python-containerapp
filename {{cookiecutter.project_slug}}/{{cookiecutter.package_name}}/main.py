from fastapi import FastAPI

app = FastAPI(title="{{ cookiecutter.project_name }}")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
