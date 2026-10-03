from fastapi import FastAPI

app = FastAPI(title="p4 demo")


@app.get("/api/health")
def health():
    return {"ok": True, "svc": "app"}


@app.get("/api/version")
def version():
    return {"v": "1.0.0"}
