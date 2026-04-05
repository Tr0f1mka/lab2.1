from unittest.mock import Mock, patch
from pytest import raises                   #type: ignore
from requests import HTTPError

from src.sources.api_source import APISource, Task
from src.contracts.task_source import TaskSource
from src.utilities.exceptions import APIError

def test_api_source():

    mock_func = Mock()
    mock_func.json.return_value = {
        "tasks": [
            {
                "id" : "ert1",
                "payload" : "Task1"
            },
            {
                "id" : "gdf2",
                "payload" : "Task2"
            },
            {
                "id" : "jhg3",
                "payload" : "I don't know what to write"
            }
        ]
    }
    mock_func.status_code = 200

    with patch("requests.get", return_value = mock_func):
        victim = APISource("test_url")
        assert isinstance(victim, TaskSource)      #проверка котракта
        assert victim.get_request() == [
            {
                "id" : "ert1",
                "payload" : "Task1"
            },
            {
                "id" : "gdf2",
                "payload" : "Task2"
            },
            {
                "id" : "jhg3",
                "payload" : "I don't know what to write"
            }
        ]

        assert list(victim.get_tasks()) == [
            Task(id="ert1", payload="Task1"),
            Task(id="gdf2", payload="Task2"),
            Task(id="jhg3", payload="I don't know what to write")
        ]

        assert isinstance(APISource.create_source("test_url"), APISource)


def test_api_source_with_http_error():

    mock_func = Mock()
    mock_func.status_code = 400
    mock_func.raise_for_status.side_effect = HTTPError()

    with patch("requests.get", return_value = mock_func):
        tester = APISource("test_url")
        with raises(APIError):
            tester.get_request()


def test_api_source_with_exception():

    mock_func = Mock()
    mock_func.json.return_value = {
        "task": [
            {
                "id" : "ert1",
                "payload" : "Task1"
            },
            {
                "id" : "gdf2",
                "payload" : "Task2"
            },
            {
                "id" : "jhg3",
                "payload" : "I don't know what to write"
            }
        ]
    }
    mock_func.status_code = 200

    with patch("requests.get", return_value = mock_func):
        victim = APISource("test_url")
        with raises(APIError):
            victim.get_request()
