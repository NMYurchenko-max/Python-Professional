from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from urllib.parse import urlparse
import time
import re


def fetch_code_tag(url):
    """Функция для получения HTML-кода страницы и анализа
     кодовых блоков на предмет полезной информации."""
    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    parsed_url = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_url)
    try:
        response = requests.head(domain, allow_redirects=True, timeout=5)
        if response.status_code != 200:
            print(
                f"Сайт недоступен или требует аутентификации. "
                f"{response.status_code}"
            )
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка подключения к сайту: {e}")
        return None

    time.sleep(1)  # Задержка в 1 секунду

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        code_blocks = soup.find_all('code')
        useful_info = []
        for code_block in code_blocks:
            if 'JSON' in code_block.text or 'selector' in code_block.text:
                useful_info.append(code_block.text.strip())

        if not useful_info:
            print("Полезная информация для парсинга не найдена.")
            return None

        for info in useful_info:
            print(info)
        return response.text

        selectors = []
        code_blocks = soup.find_all('code')
        for block in code_blocks:
            if ('class="vacancy-card"' in block.text or
               'data-vacancy' in block.text):
                selectors.append(block.text.strip())

            matches = re.findall(r'class="([^"]*)"', block.text)
            selectors.extend(matches)
            selectors.append(block.text.strip())

            matches = re.findall(r'data-([^=]*)', block.text)
            selectors.extend(matches)
            selectors.append(block.text.strip())

            matches = re.findall(r'selery="([^"]*)"', block.text)
            selectors.extend(matches)
            selectors.append(block.text.strip())

            matches = re.findall(r'sity="([^"]*)"', block.text)
            selectors.extend(matches)
            selectors.append(block.text.strip())

            matches = re.findall(r'company="([^"]*)"', block.text)
            selectors.extend(matches)
            selectors.append(block.text.strip())

        if not selectors:
            print("Селекторы не найдены.")
        return selectors

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP ошибка: {http_err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Ошибка при выполнении запроса: {err}")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def extract_code_blocks(url):
    """Извлекать кодовые блоки с указанной страницы."""
    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    parsed_url = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_url)
    try:
        response = requests.head(domain, allow_redirects=True, timeout=5)
        if response.status_code != 200:
            print(
                f"Сайт недоступен или требует аутентификации. "
                f"{response.status_code}"
            )
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка подключения к сайту: {e}")
        return None

    time.sleep(1)  # Задержка в 1 секунду
    response = requests.get(url, headers=headers)

    try:
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        code_tags = soup.find_all('code')
        for i, code_tag in enumerate(code_tags, start=1):
            print(f"Code block {i}:")
            print(code_tag.get_text())
            print()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Ошибка при выполнении запроса: {err}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    return None


if __name__ == "__main__":
    base_url = 'https://spb.hh.ru/search/vacancy'
    params = {
        'text': 'python django flask',
        'ored_clusters': 'true',
        'enable_snippets': True,
        'area': '1&area=2',
        'page': 0,
        'per_page': 20
    }
    full_url = f"{base_url}?{'&'.join(
                [f'{key}={value}' for key, value in params.items()])}"

    html_content = fetch_code_tag(full_url)
    print(html_content)

    html_content_1 = extract_code_blocks(full_url)
    print(html_content_1)
