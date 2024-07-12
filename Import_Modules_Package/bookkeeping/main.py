from application.db.people import get_employees
from application.salary import calculate_salaries

from datetime import datetime
from pprint import pprint


def datatime_convert(unix_time):
    """Конвертирует время из формата UNIX в читаемый формат."""
    dt_object = datetime.fromtimestamp(int(unix_time))

    # Форматируем дату в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС с учетом зоны
    formatted_date = dt_object.strftime(
        '%Y-%m-%d_at_%H-%M-%S').replace('-', '_')
    print(formatted_date)
    return formatted_date


def main():
    employees = get_employees()
    pprint(employees)
    salaries = calculate_salaries(employees)
    print("Зарплаты сотрудников:", salaries)
    print(f"Сумма зарплат: {sum(salaries)}")
    print(f"Средняя зарплата:  {sum(salaries) / len(salaries)}")
    print()

    current_date = datetime.now()
    print(f"Текущая дата: {current_date}")
    print(current_date.strftime("%d-%m-%Y_at_ %H:%M:%S"))
    print()
    datatime_convert(123456789)
    print()


if __name__ == "__main__":
    main()
