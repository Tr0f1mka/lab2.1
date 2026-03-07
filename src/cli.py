from typer import Typer, Argument, Option, BadParameter        #type: ignore

from src.contracts.task_source import TaskSource
from src.sources.registry import REGISTRY
from src.sources.api_source import APISource                   # noqa: F401
from src.sources.generator_source import GeneratorTask        # noqa: F401
from src.sources.jsonl_source import JSONLinesSource           # noqa: F401


app = Typer()

def build_source(source: str, file: str | None) -> TaskSource:
    """
    Создание экземпляра источника задач
    :param source: Строка - тип источника
    :param file: Строка - путь к файлу или ничего
    :return: Экземпляр источника задач
    """

    manufacture = REGISTRY[source]
    if source == "jsonl":
        return manufacture(file)
    return manufacture()


def check_type_source(source: str) -> str | None:
    """
    Проверяет тип источника
    :param source: Строка - тип источника
    :return: Эта же строка или ничего
    """
    if source in REGISTRY.keys():
        return source
    raise BadParameter(f"Источника {source} не существует")


@app.command(help="Отобразить типы источников")
def types() -> None:
    for i in REGISTRY.keys():
        print(i)


@app.command(help="Получить задачи")
def get_tasks(
    source: str = Argument(None, help=f"Тип источика: {", ".join(REGISTRY.keys())}", callback=lambda x: check_type_source(x)),
    file: str = Option(None, "-f", "--file", help="Имя файла источника задач")
) -> None:

    ready_source = build_source(source, file)
    for i in ready_source.get_tasks():
        print(f"ID: {i.id:8}    PAYLOAD: {i.payload}")
