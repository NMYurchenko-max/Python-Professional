import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv


def get_vacancies(url):
    """ Функция для разбора HTML-кода страницы и извлечения
     информации о вакансиях. """
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        # Вызывает исключение в случае ошибки ответа
        return response.text
    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        raise


# Функция для парсинга вакансий
def parse_vacancies(html_content):
    """ Функция для парсинга HTML-кода страницы и извлечения
     информации о вакансиях. """
    soup = BeautifulSoup(html_content, 'lxml')
    vacancies_list = []
    items = soup.find_all(
        'div', class_='vacancy-card--z_UXteNo7bRGzxWVcL7y')
    for item in items:
        title = item.find('a', class_='bloko-link').text
        link = item.find('a', class_='bloko-link')['href']
        description = item.find('div', class_='g-user-content').text

        salary_element = item.find('span', class_='bloko-header-section-3')
        salary = salary_element.text.strip() if salary_element else ""

        company = item.find(
            'span', class_='bloko-header-section-2').text if item.find(
            'span', class_='bloko-header-section-2') else 'Не указан'

        city = item.find(
            'span', class_='bloko-header-section-3').text if item.find(
            'span', class_='bloko-header-section-3') else 'Не указана'

        metro = item.find(
            'span', class_='bloko-header-section-3').text if item.find(
            'span', class_='bloko-header-section-3') else 'Не указана'

        vacancies_list.append({
            'title': title,
            'link': link,
            'description': description,
            'salary': salary,
            'company': company,
            'city': city,
            'metro': metro
        })
    print(f'Найдено {len(vacancies_list)} вакансий на странице.')
    return vacancies_list


# Функция для записи вакансий в CSV
def write_vacancies_to_file(vacancies):
    """ Функция для записи вакансий в CSV файл. """
    if not vacancies:
        print("Нет данных для записи в файл.")
        return
    with open('Web-SCRAPING/vacancies.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(
            file, fieldnames=[
                'title',
                'link',
                'salary',
                'company',
                'city',
                'metro',
                'description'
            ]
        )
        writer.writeheader()
        writer.writerows(vacancies)
    print("Данные записаны в файл: 'Web-SCRAPING/vacancies.csv'.")

    # Вывод списка уникальных данных
    for vacancies in vacancies:
        print(vacancies)


# Точка входа
if __name__ == '__main__':
    base_url = 'https://spb.hh.ru/search/vacancy'
    params = {
        'text': 'python django flask',
        'salary': 'ored_clusters=true',
        'enable_snippets': 'true',
        'area': '1&area=2',
        'page': 0,
        'per_page': 20
    }
    full_url = f"{base_url}?{'&'.join(
        [f'{key}={value}' for key, value in params.items()])}"
    html_content = get_vacancies(full_url)
    vacancies = parse_vacancies(html_content)
    write_vacancies_to_file(vacancies)
    print("Программа завершена.")
