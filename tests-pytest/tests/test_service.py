import pytest
import source.service as service
import unittest.mock as mock
import requests


@mock.patch("source.service.get_user")
def test_get_user(mock_get_user):
    mock_get_user.return_value = "Mocked Alice"
    username = service.get_user(2)

    assert username == "Mocked Alice"


@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1, "name": "Alice"}]
    mock_get.return_value = mock_response
    data = service.get_users()
    assert data == [{"id": 1, "name": "Alice"}]


@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    with pytest.raises(requests.HTTPError):
        service.get_users()
