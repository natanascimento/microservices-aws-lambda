import pytest

from app.main import lambda_handler


@pytest.fixture()
def mock_event():
  return {"first_name": "Natan",
          "last_name": "Nascimento"}


def test_lambda_handler_return(mock_event):

  response = lambda_handler(mock_event, "")

  assert response.get('message') == 'Hello Natan Nascimento!'
