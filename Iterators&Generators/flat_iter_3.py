class FlatIterator:
    """
    Итератор, который преобразует вложенные списки
    в один список.
    """
    def __init__(self, list_of_list):
        """
        Инициализация итератора.
        :param list_of_list: Список списков для преобразования.
        Используем стековый подход,
        где каждый внутренний список
        будет помещаться в стек для последующей обработки
        """
        self.list_of_list = list_of_list
        # создаем список из входного списка
        self.stack = [[list_of_list, 0]]
        # Используем список для хранения состояния стека
        #  и индекса текущего списка внутри стека

    def __iter__(self):
        """
        Возвращает сам себя как итерируемый объект.
        """
        return self

    def __next__(self):
        """
    Возвращает следующий элемент списка или вызывает исключение
    StopIteration, если больше нет элементов для возврата.
        """
        while self.stack:
            sublist, index = self.stack[-1]
            try:
                item = sublist[index]
                if isinstance(item, list):
                    # Если элемент является списком, добавляем его в стек
                    # для дальнейшей обработки
                    self.stack.append([item, 0])
                    # Добавляем новый список в стек без увеличения индекса
                else:
                    # Если элемент не является списком, возвращаем его
                    self.stack[-1][1] += 1
                    # Переходим к следующему элементу в текущем списке
                    return item
                index += 1  # Увеличиваем индекс для следующего элемента
                self.stack[-1][1] = index
            except IndexError:
                # Если достигнут конец текущего списка, удаляем его из стека
                self.stack.pop()
        else:
            raise StopIteration  # Если стек пуст, завершаем итерацию


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
