from unittest.mock import patch

from starlette.testclient import TestClient

from src.main import get_application
from src.service_llm import LARGE_TEXT_THRESHOLD

app = get_application()
client = TestClient(app)

def test_summarize_empty_text():
    response = client.post(
        "/llm/summarize",
        json={"text": ""}
    )

    assert response.status_code == 422
    error_detail = response.json()["detail"]
    assert any(
        "text" in str(error["loc"]) and "String should have at least" in error["msg"]
        for error in error_detail
    )


@patch("src.router.llm.summarize_small_text")
def test_summarize_routing_by_text_size(mock_summarize_small):
    mock_summarize_small.return_value = "Small text summary"

    small_text = "Small text " + "X" * 90  # Ensure it's at least 100 characters
    response_small = client.post(
        "/llm/summarize",
        json={"text": small_text}
    )

    expected = {"summary": "Small text summary"}

    assert response_small.status_code == 200
    assert response_small.json() == expected


@patch("src.router.llm.summarize_large_text")
def test_summarize_large_routing_by_text_size(mock_summarize_large):
    mock_summarize_large.return_value = "Large text summary"

    large_text = "X" * (LARGE_TEXT_THRESHOLD + 1)  # Exceed THRESHOLD by 1
    response_large = client.post(
        "/llm/summarize",
        json={"text": large_text}
    )

    expected = {"summary": "Large text summary"}

    assert response_large.status_code == 200
    assert response_large.json() == expected

    mock_summarize_large.assert_called_once_with(large_text)
