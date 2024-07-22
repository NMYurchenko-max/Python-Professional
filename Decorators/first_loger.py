import os
from datetime import datetime


def logger(old_function):
    """
    Декоратор для логирования информации о вызове другой функции.
    Параметры:
    - old_function: Исходная функция, которую нужно декорировать.
     Возвращает:
    - Результат вызова исходной функции.
     Логирует:
    - Временную метку момента вызова функции.
    - Имя вызываемой функции.
    - Переданные аргументы функции.
    - Значение, возвращаемое функцией.
    Записывает логи в файл 'main.log'.
    """
    def new_function(*args, **kwargs):
        # Вызов оригинальной функции с переданными аргументами
        result = old_function(*args, **kwargs)
        # Получение текущего времени
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Получение имени оригинальной функции
        function_name = old_function.__name__
        # Преобразование аргументов в строковое представление
        args_str = ', '.join([repr(arg) for arg in args])
        # Преобразование ключевых аргументов в строковое представление
        kwargs_str = ', '.join([
            f'{key}={repr(val)}'
            for key, val in kwargs.items()
        ])
        # Комбинирование аргументов и ключевых аргументов
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        # Преобразование результата в строковое представление
        return_value = repr(result)

        # Конструкция сообщения лога
        log_message = (
            f'{timestamp} - '
            f'{function_name}({all_args}) -> '
            f'{return_value}\n'
        )
        # Добавление сообщения лога в файл 'main.log'
        with open('Decorators/main.log', 'a') as log_file:
            log_file.write(log_message)

        # Вывод подтверждающего сообщения
        print('Данные записаны в файл main.log')

        # Возврат результата оригинальной функции
        return result

    # Возврат новой функции, которая оборачивает оригинальную
    return new_function


def test_1():

    path = 'Decorators/main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'
    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()
