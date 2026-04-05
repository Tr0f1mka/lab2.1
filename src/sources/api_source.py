from typing import Iterable
import requests

from src.contracts.task import Task
from src.sources.registry import add_source
from src.utilities.generator_id import generator_id
from src.utilities.logger import logger
from src.utilities.exceptions import APIError


class APISource:
    """
    Источник из API
    """
    url: str

    def __init__(self, url: str) -> None:
        """
        Инициализация источника
        :param url: Строка - URL-адес
        :return: Ничего
        """

        self.url = url


    def get_request(self) -> list[dict[str, str]]:
        """
        Заглушка с данными
        :return: Словарь с задачами
        """

        try:
            # API
            response = requests.get(self.url)
            response.raise_for_status()

            return response.json()["tasks"]

            # Заглушка
            # return [
            #     {"id": "id1", "payload": "Task1"},
            #     {"id": "id2", "payload": "Task2"},
            #     {"id": "id3", "payload": "Task3"}
            # ]

        except requests.HTTPError as e:
            logger.error(f"API-request error: {e}")
            raise APIError(f"API-request error: {e}")
        except Exception as e:
            logger.error(f"API-request error: {e}")
            raise APIError(f"API-request error: {e}")


    def get_tasks(self) -> Iterable[Task]:
        """
        Получает задачи из API-заглушки
        :return: Итератор задач
        """

        logger.info("Used: APISource")
        response = self.get_request()
        logger.info("The task dictionary has been received")
        for i, task in enumerate(response, start=1):
            yield Task(
                id = task.get("id", generator_id()),
                payload = task.get("payload", "")
            )


    @add_source("api")
    def create_source(url: str) -> "APISource":
        """
        Создаёт экземпляр генератора задач
        :param url: Строка - URL-адрес
        :return: Генератор задач
        """

        return APISource(url)
