from fastapi.testclient import TestClient

from app.main import app

api = TestClient(app)


def test_health():
    r = api.get("/api/health")
    assert r.json() == {"ok": True, "svc": "app"}


def test_version():
    assert api.get("/api/version").json() == {"v": "1.0.0"}


def test_unknown():
    assert api.get("/api/nope").status_code == 404
