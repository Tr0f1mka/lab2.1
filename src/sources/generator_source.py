from collections.abc import Iterable
from random import randint, choice

from src.contracts.task import Task
from src.constants import EXAMPLES_TASKS
from src.utilities.generator_id import generator_id
from src.sources.registry import add_source


class GeneratorTask:
    """
    Программный генератор задач
    """

    def get_tasks(self) -> Iterable[Task]:
        """
        Генерирует задачи
        :return: Итератор задач
        """

        for i in range(randint(5, 10)):
            id = generator_id(i)
            payload = choice(EXAMPLES_TASKS)
            yield Task(id = id, payload = payload)


@add_source(name = "gen_tasks")
def create_generator_tasks() -> GeneratorTask:
    """
    Создаёт экземпляр генератора задач
    :return: Генератор задач
    """

    return GeneratorTask()
