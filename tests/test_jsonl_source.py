import pytest   #type: ignore
import json
from random import seed

from src.sources.jsonl_source import JSONLinesSource, Task, JSONLinesError, create_jsonl_source
from src.contracts.task_source import TaskSource


test_case = [
    {"id":"1", "payload": "Task1"},
    {"id":"2", "payload": "Task2"},
    {"id":"3", "payload": "Task3"},
]


@pytest.fixture
def test_file(tmp_path):
    file_path = tmp_path / "test.jsonl"
    with open(file_path, "w", encoding="utf-8") as f:
        for i in test_case:
            f.write(json.dumps(i, ensure_ascii=False) + "\n\n")

    yield str(file_path)


def test_jsonl_source(test_file):
    test = JSONLinesSource(path=test_file)

    seed(0)
    assert isinstance(test, TaskSource)
    assert list(test.get_tasks()) == [Task(id=task.get("id"), payload=task.get("payload")) for task in test_case]
    assert isinstance(create_jsonl_source(test_file), JSONLinesSource)


def test_parser_with_error():
    with pytest.raises(JSONLinesError):
        JSONLinesSource.parser("YTERWRTRYTJ", 1, "file.txt")


def test_json_source_with_error_not_jsonl():
    test = JSONLinesSource(path="file.txt")
    with pytest.raises(JSONLinesError):
        list(test.get_tasks())


def test_json_source_with_error_read():
    test = JSONLinesSource(path="file.jsonl")
    with pytest.raises(JSONLinesError):
        list(test.get_tasks())
