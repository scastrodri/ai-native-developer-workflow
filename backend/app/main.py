from fastapi import FastAPI

app = FastAPI(title="Weekly Team Feedback Tool")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
