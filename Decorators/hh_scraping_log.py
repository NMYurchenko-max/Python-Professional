import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv

from logging_decorator import logger


def get_vacancies(url):
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        raise


def parse_vacancies(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    vacancies_list = []
    items = soup.find_all('div', class_='vacancy-card--z_UXteNo7bRGzxWVcL7y')
    for item in items:
        title = item.find('a', class_='bloko-link').text
        link = item.find('a', class_='bloko-link')['href']
        description = item.find('div', class_='g-user-content').text
        salary = item.find(
            'span', class_='bloko-header-section-3').text if item.find(
                'span', class_='bloko-header-section-3') else 'Не указана'
        city = item.find(
            'span', class_='bloko-header-section-3').text if item.find(
                'span', class_='bloko-header-section-3') else 'Не указан'
        company = item.find(
            'span', class_='bloko-header-section-3').text if item.find(
                'span', class_='bloko-header-section-3') else 'Не указан'
        date = item.find(
            'span', class_='bloko-header-section-3').text if item.find(
                'span', class_='bloko-header-section-3') else 'Не указана'
        vacancies_list.append({
            'title': title,
            'link': link,
            'description': description,
            'salary': salary,
            'city': city,
            'company': company,
            'date': date
        })
    print(f'Найдено {len(vacancies_list)} вакансий на странице.')
    return vacancies_list


@logger('Decorators/my_log.log')
def write_vacancies_to_file(vacancies):
    if not vacancies:
        print("Нет данных для записи в файл.")
        return
    with open('Decorators/vacancies.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=[
            'title',
            'link',
            'description',
            'salary',
            'city',
            'company',
            'date'
            ]
        )
        writer.writeheader()
        writer.writerows(vacancies)
    print("Данные записаны в файл: 'vacancies.csv'.")


if __name__ == '__main__':
    base_url = 'https://spb.hh.ru/search/vacancy'
    params = {
        'text': 'python django flask',
        'salary': 'ored_clusters=true',
        'enable_snippets': True,
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
