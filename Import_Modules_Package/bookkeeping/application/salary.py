def calculate_salaries(employees):
    # Например, простой расчет на основе базовой ставки
    base_salaries = {"manager": 50000, "developer": 60000, "designer": 55000}
    salaries = [
        base_salaries.get(employee["position"], 0) for employee in employees]
    return salaries


def get_average(salaries):
    return sum(salaries) / len(salaries)


def get_min(salaries):
    return min(salaries)


def get_max(salaries):
    return max(salaries)


def get_median(salaries):
    return sorted(salaries)[len(salaries) // 2]
