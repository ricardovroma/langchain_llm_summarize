from starlette.testclient import TestClient

from src.main import get_application

app = get_application()
client = TestClient(app)


def test_when_healthcheck_then_success():
    response = client.get("/healthcheck")

    assert response.status_code == 200
    assert response.text == "Healthy"
