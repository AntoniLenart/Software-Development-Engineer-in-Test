import pytest
from api_main import get_weather


def test_get_weather(mocker):
    mock_get = mocker.patch("api_main.requests.get")

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature": 20, "condition": "Sunny"}

    result = get_weather("London")

    assert result == {"temperature": 20, "condition": "Sunny"}
    mock_get.asssert_called_once_with("https://api.weather.com/v1/London")
