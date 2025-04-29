import pytest
from service import UserService, APIClient


def test_get_username(mocker):
    mock_api_client = mocker.Mock(spec=APIClient)

    mock_api_client.get_user_data.return_value = {"id": 1, "name": "John Doe"}

    service = UserService(mock_api_client)
    result = service.get_username(1)
    assert result == "JOHN DOE"
    mock_api_client.get_user_data.assert_called_once_with(1)
