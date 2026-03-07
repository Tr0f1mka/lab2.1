from collections.abc import Iterable
from typing import Protocol, runtime_checkable

from src.contracts.task import Task


@runtime_checkable
class TaskSource(Protocol):
    """
    Класс источника. Задаёт общий контракт get_tasks для всех источников
    """

    def get_tasks(self) -> Iterable[Task]:
        ...
