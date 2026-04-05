import uuid

def generator_id() -> str:
    """
    Генератор ID
    :param ind: Номер задачи в цикле
    :return: Строка - ID
    """

    return str(uuid.uuid1())
