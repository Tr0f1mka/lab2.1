from typing import Iterable

from src.contracts.task import Task
from src.sources.registry import add_source
from src.utilities.exceptions import JSONLinesError
from src.utilities.generator_id import generator_id
from src.utilities.logger import logger
from src.utilities.jsonl_parser import parser


class JSONLinesSource:
    """
    Извлекатель задач из файла формата JSON Lines
    """

    path: str

    def __init__(self, path: str) -> None:
        """
        Инициализация источника
        :param path: Строка - имя файла
        """

        self.path = path

    def get_tasks(self) -> Iterable[Task]:
        """
        Читает задачи из файла JSON Lines
        :return: Итератор задач
        """

        logger.info("Used: JSONLinesSource")
        if self.path[-6:] != ".jsonl":
            logger.error(f"Incorrect file name: \"{self.path}\"")
            raise JSONLinesError(f"Incorrect file name: \"{self.path}\"")

        try:
            with open(self.path, "r", encoding="utf-8") as f:
                i = 0
                for line in f.readlines():
                    i += 1
                    line = line.strip()
                    if not line:
                        continue
                    task = parser(line, i, self.path)
                    yield Task(
                        id = task.get("id", generator_id()),
                        payload = task.get("payload", "Task has not defined")
                    )
        except Exception as error:
            raise JSONLinesError(error)


    @add_source("jsonl")
    def create_source(file: str) -> "JSONLinesSource":
        """
        Создаёт экземпляр генератора задач
        :return: Генератор задач
        """

        return JSONLinesSource(path=file)
