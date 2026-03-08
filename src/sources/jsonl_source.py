from dataclasses import dataclass
from typing import Iterable
import json

from src.contracts.task import Task
from src.sources.registry import add_source
from src.utilities.exceptions import JSONLinesError
from src.utilities.generator_id import generator_id
from src.utilities.logger import logger


@dataclass(frozen=True)
class JSONLinesSource:
    path: str

    @staticmethod
    def parser(line: str, line_index: int, file: str) -> dict[str, str]:
        """
        Парсер JSON-строк
        :param line: Строка, которую нужно распарсить
        :param line_index: Целое число - номер строки(для логов ошибок)
        :param file: Строка - имя файла(для логов ошибок)
        :return: Распарсенный словарь
        """

        try:
            return json.loads(line)
        except json.JSONDecodeError as error:
            raise JSONLinesError(f"File: {file}; Line: {line_index}; Error: {error}")


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
                    task = self.parser(line, i, self.path)
                    yield Task(
                        id = task.get("id", generator_id(i)),
                        payload = task.get("payload", "Task has not defined")
                    )
        except Exception as error:
            raise JSONLinesError(error)


@add_source("jsonl")
def create_jsonl_source(file: str) -> JSONLinesSource:
    return JSONLinesSource(path=file)
