from random import randint, choice

from src.constants import ALPHABET


def generator_id(ind: int) -> str:
    """
    Генератор ID
    :param ind: Номер задачи в цикле
    :return: Строка - ID
    """

    return "".join([choice(ALPHABET) for x in range(randint(1, 4))]) + str(ind)
