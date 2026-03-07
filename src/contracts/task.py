from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Task:
    """
    Класс задачи. Имеет поля id и payload
    """

    id: str
    payload: str
