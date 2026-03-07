from typing import Callable

from src.contracts.task_source import TaskSource


"""
--------------------------
----Регистр источников----
--------------------------
"""


SourcePattern = Callable[..., TaskSource]
REGISTRY: dict[str, SourcePattern] = {}


def add_source(name: str) -> Callable[[SourcePattern], SourcePattern]:
    """
    Декоратор, добавляющий функцию создания в регистр(фабрика)
    :param name: Строка - ключ источника
    :return: Источник задач
    """

    def decorator(source: SourcePattern) -> SourcePattern:
        """
        Функция-обёртка для функции add_source
        :param source: Функция сборки источника
        :return: Источник задач
        """

        REGISTRY[name] = source
        return source
    return decorator
