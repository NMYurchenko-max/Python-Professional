import types


def flat_generator(list_of_list):
    """
    Генератор, который преобразует вложенные списки в один плоский список.
    Args:
    list_of_list (list): Список, содержащий элементы, включая вложенные списки.
    Yields:
    object: Элементы списка, преобразованные в один плоский список.

    """
    for item in list_of_list:
        if isinstance(item, list):
            # Проверка - если элемент является списком, рекурсивно
            # вызываем генератор для этого списка
            for sub_item in flat_generator(item):
                yield sub_item
                # Возвращение элемента из вложенного списка
        else:
            # Если элемент не является списком, возвращаем его
            yield item


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
