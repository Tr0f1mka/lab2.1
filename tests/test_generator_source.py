from random import seed

from src.sources.generator_source import GeneratorTask, create_generator_tasks, Task
from src.contracts.task_source import TaskSource


def test_generator_source():
    seed(0)
    test = GeneratorTask()

    assert isinstance(test, TaskSource)
    assert list(test.get_tasks()) == [Task(id="biqp0", payload="Пережить семестр"),
                                      Task(id="pls1", payload="Сделать вёрстку сайта"),
                                      Task(id="je2", payload="Понять смысл жизни"),
                                      Task(id="rwz3", payload="Придумать ещё примеры задач для генератора"),
                                      Task(id="jd4", payload="Понять смысл жизни"),
                                      Task(id="prd5", payload="Освоить навык Израна"),
                                      Task(id="ktug6", payload="Дописать клон Undertale"),
                                      Task(id="oqib7", payload="Дописать клон Undertale")]
    assert isinstance(create_generator_tasks(), GeneratorTask)
