from datetime import datetime
from application import salary
from application.db import people
from bootlocale.main import datatime_convert


# Это вариант импорта файлов, а не функций (кроме main - конфликт имен)
def main():
    employees = people.get_employees()
    print(employees)
    salaries = salary.calculate_salaries(employees)
    print("Зарплаты сотрудников:", salaries)
    print(f"Сумма зарплат: {sum(salaries)}")
    print(f"Средняя зарплата:  {sum(salaries) / len(salaries)}")
    print()

    current_date = datetime.now()
    print(f"Текущая дата: {current_date}")
    print(current_date.strftime("%d-%m-%Y_at_ %H:%M:%S"))
    print()

    datatime_convert(123456789)


if __name__ == "__main__":
    main()

    """
Конструкция:
from package.module import *
Не рекомендуется к применению.
Может привести к конфликту имен (2 main)
у меня конструкция не сработала:
ModuleNotFoundError: No module named 'package'
НЕ работает и вариант импорта из явно указанного пакета:
ModuleNotFoundError: No module named 'bookkeeping'
(сообщение VSC), даже в текущем варианте ????
Проблема сопоставима с моим проектом...
А в Pycharm текущая конструкция работает!?
В чем проблема? 
    """
