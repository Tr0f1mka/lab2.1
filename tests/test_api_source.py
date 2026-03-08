from src.sources.api_source import APISource, Task, create_api_source
from src.contracts.task_source import TaskSource

def test_api_source():

    victim = APISource()
    assert isinstance(victim, TaskSource)      #проверка котракта
    assert victim.stub() == [
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

    assert isinstance(create_api_source(), APISource)
