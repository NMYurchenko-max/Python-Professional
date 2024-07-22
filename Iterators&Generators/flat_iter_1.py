
class FlatIterator:
    """
    Итератор, который преобразует список списков в плоский список.
    """

    def __init__(self, list_of_list):
        """
        Инициализация итератора.
        :param list_of_list: Список списков для преобразования.
        Используем стековый подход, где каждый внутренний список
        будет помещаться в стек для последующей обработки
        """
        self.stack = iter(list_of_list)
        # Создаем иитератор из входного списка
        try:
            first_list = next(self.stack)
            # Извлекаем первый список из стека
        except StopIteration:
            first_list = []
            # Если стек пустой, то возвращаем пустый список
        self.current_list = iter(first_list)
        # Создаем итератор из первого списка для перебора элементов

    def __iter__(self):
        """
        Возвращает сам себя как итерируемый объект.
        """
        return self

    def __next__(self):
        """
        Возвращает следующий элемент списка или вызывает исключение
        StopIteration, если больше нет элементов для возврата.
        Цикл while True используется для повторения попыток получения
        следующего элемента до тех пор, пока элемент не будет найден
        """
        while True:
            try:
                value = next(self.current_list)
                return value
                # Возвращаем следующий элемент из текущего списка,
                # если он найден - возвращается
            except StopIteration:
                #  Обрабатываем исключение, которое возникает,
                # если текущий список исчерпан
                if not self.stack:
                    raise StopIteration
                # Проверяем, если стек пустой, то выходим из цикла
                self.current_list = iter(next(self.stack))
                # Иначе возвращаем следующий элемент из стека


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
