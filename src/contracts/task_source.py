from collections.abc import Iterable
from typing import Protocol, runtime_checkable

from src.contracts.task import Task


@runtime_checkable
class TaskSource(Protocol):
    """
    Класс источника. Задаёт общие контракты get_tasks и create_source для всех источников
    """

    def get_tasks(self) -> Iterable[Task]:
        ...

    def create_source(self) -> "TaskSource":
        ...
