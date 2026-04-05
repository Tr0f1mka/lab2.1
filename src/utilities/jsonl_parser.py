import json
from src.utilities.exceptions import JSONLinesError

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
