import types


def flat_generator(list_of_lists):
    """
    Генератор, который преобразует список списков в плоский список.
    """
    # Создаем итератор из входного списка списков.
    # Это будет наш "стек" для обработки.
    stack = iter(list_of_lists)
    try:
        # Попытка получить первый список из стека.
        # Если стек пуст, возникает исключение StopIteration.
        first_list = next(stack)
    except StopIteration:
        # Если стек пуст, начинаем с пустого списка,
        # чтобы избежать ошибок при итерации.
        first_list = []
    # Создаем итератор для первого списка, чтобы начать обработку.
    current_list_iter = iter(first_list)
    # Главный цикл генератора.
    while True:
        try:
            # Попытка получить следующий элемент из текущего списка.
            value = next(current_list_iter)
            # Если элемент успешно получен, передаем его через yield.
            yield value
        except StopIteration:
            # Если текущий список исчерпан, пытаемся получить следующий
            #  список из стека.
            try:
                # Получаем следующий список из стека для обработки.
                current_list_iter = iter(next(stack))
            except StopIteration:
                # Если стек пуст и нет следующего списка, завершаем цикл.
                break
            else:
                # Если удалось получить новый список, продолжаем цикл с ним.
                continue


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
