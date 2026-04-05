from random import seed

from src.sources.generator_source import GeneratorTask, Task
from src.contracts.task_source import TaskSource


def test_generator_source(mocker):

    mock_func = mocker.patch("uuid.uuid1")
    mock_func.return_value = "id1"

    seed(0)
    test = GeneratorTask()

    assert isinstance(test, TaskSource)
    assert list(test.get_tasks()) == [
            Task(id='id1', payload='Пережить семестр'),
            Task(id='id1', payload='Сделать лабу'),
            Task(id='id1', payload='Изучить Angular'),
            Task(id='id1', payload='Дописать клон Undertale'),
            Task(id='id1', payload='Отдохнуть'),
            Task(id='id1', payload='Пережить семестр'),
            Task(id='id1', payload='Изучить Angular'),
            Task(id='id1', payload='Отдохнуть')
        ]
    assert isinstance(GeneratorTask.create_source(), GeneratorTask)
