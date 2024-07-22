import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json
import time
# import webbrowser
from urllib.parse import urlparse, urlencode


def fetch_vacancies(url):
    """ Функция для получения HTML-кода страницы.
    Проверяет доступность URL,
    выполняет задержку перед запросом и обрабатывает ошибки. """
    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    # Проверяем доступность URL
    parsed_url = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_url)
    try:
        response = requests.head(domain, allow_redirects=True, timeout=5)
        if response.status_code != 200:
            print(f"Сайт недоступен или требует аутентификации. {''}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка подключения к сайту: {e}")
        return None

    # Задержка перед выполнением запроса
    time.sleep(1)  # Задержка в 1 секунду

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def extract_city_and_metro(address_text, soup):
    """ Функция для извлечения города и метро из текста адреса. """
    city = ""
    metros = []
    if ',' in address_text:
        city = address_text.split(',')[0].strip()
    metro_elements = soup.select('.metro-station')
    for metro in metro_elements:
        metros.append(metro.text.strip())
    return city, metros


def parse_vacancies(full_url):
    """ Функция для разбора HTML-кода страницы и
    извлечения информации о вакансиях. """
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    try:
        response = requests.get(full_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        vacancies = []
        vacancy_items = soup.find_all(
            'div', class_="vacancy-card--z_UXteNo7bRGzxWVcL7y font-inter")
        if not vacancy_items:
            print("Не найдено вакансий.")
            return []
        for item in vacancy_items:
            title_element = item.find(
                'span', class_='serp-item__title-link-wrapper')
            if title_element:
                # Находим тег <a> внутри title_element
                link_element = title_element.find('a')
                if link_element:
                    # Получаем атрибут href из найденного тега <a>
                    link = link_element['href']
                    title = title_element.text.strip()
                else:
                    print("Тег <a> не найден внутри title_element")
                    continue
            else:
                print("Элемент с заголовком вакансии не найден")
                continue

            company_element = item.find(
                'a', {'data-qa': 'vacancy-serp__vacancy-employer'})
            company_name = (
                company_element.text.strip() if company_element else "")

            address_element = item.find(
                'span', {'data-qa': 'vacancy-view-raw-address'})
            address_text = (
                address_element.text.strip() if address_element else "")
            city, metros = extract_city_and_metro(address_text, soup)

            salary_element = item.find(
                'span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
            salary = salary_element.text.strip() if salary_element else ""

            key_skills = item.find(
                'div', {
                    'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'})
            key_skills = key_skills.text.strip() if key_skills else ""

            # Добавляем вакансию в список
            vacancies.append({
                'text': 'python, django, flask',
                'title': title,
                'link': link,
                'company': company_name,
                'city': city,
                # 'metros': metros,
                'salary': salary,
                'key_skills': key_skills
            })
        return vacancies
    except requests.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return []
    except Exception as e:
        # Обработка всех других исключений
        print(f"Произошла ошибка: {e}")
        return []


def main():
    """ Главная функция, объединяющая все шаги парсинга. """
    base_url = 'https://spb.hh.ru/search/vacancy'
    params = {
        'text': 'python django flask',
        'ored_clusters': 'true',
        'enable_snippets': 'true',
        'area': '1, 2',
        'hhmFrom': 'vacancy_search_list',
        'hhmFromLabel': 'vacancy_search_line',
        'page': 0,
        'per_page': 20
    }
    full_url = f"{base_url}?{urlencode(params)}"
    vacancies = parse_vacancies(full_url)
    with open('WEB-SCRAPING/vacancies.json', 'w', encoding='utf-8') as f:
        json.dump(vacancies, f, ensure_ascii=False, indent=4)
    print(f'Найдено {len(vacancies)} вакансий, создан файл vacancies.json')


# Открываем в браузере вакансию
"""    for vacancy in vacancies:
        webbrowser.open_new_tab(vacancy['link'])

"""
if __name__ == "__main__":
    main()
