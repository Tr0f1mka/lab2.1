from typing import Iterable

from src.contracts.task import Task
from src.sources.registry import add_source
from src.utilities.generator_id import generator_id


class APISource:
    """
    Источник из API-заглушки
    """

    @staticmethod
    def stub() -> list[dict[str, str]]:
        """
        Заглушка с данными
        :return: Словарь с задачами
        """

        return [
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


    def get_tasks(self) -> Iterable[Task]:
        """
        Получает задачи из API-заглушки
        :return: Итератор задач
        """

        response = self.stub()
        for i, task in enumerate(response, start=1):
            yield Task(
                id = task.get("id", generator_id(i)),
                payload = task.get("payload", "")
            )


@add_source("api")
def create_api_source() -> APISource:
    return APISource()
