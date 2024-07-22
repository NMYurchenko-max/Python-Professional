from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import csv
from selenium import webdriver
import os


driver = webdriver.Chrome()
print(driver.capabilities['browserVersion'])
driver.quit()


def wait_element(browser, delay_seconds=1, by=By.CLASS_NAME, value=None):
    return WebDriverWait(browser, delay_seconds).until(
        EC.presence_of_element_located((by, value))
    )


path = ChromeDriverManager().install()
Servicepath = Service(executable_path=path)
browser = Chrome(service=Servicepath)
base_url = 'https://spb.hh.ru/search/vacancy'

params = {
    'text': 'python django flask',
    'salary': 'ored_clusters=true',
    'enable_snippets': True,
    'area': '1, 2',
    'hhmFrom': 'vacancy_search_list',
    'hhmFromLabel': 'vacancy_search_line',
    'from': 'suggest_popup',
    'items_on_page': 20,
    'field': 'name',
}

# Переход на страницу поиска вакансий
browser.get(
    f"{base_url}?{'&'.join(
        [f'{key}={value}' for key, value in params.items()])}")

# Ожидание появления кнопки поиска и клик по ней
wait_element(browser, by=By.CLASS_NAME, value='bloko-button').click()


vacancy_list = browser.find_elements(
    By.CLASS_NAME, "vacancy-card--z_UXteNo7bRGzxWVcL7y")

parser_data = []

for i in range(len(vacancy_list)):
    try:
        # Поиск элемента с ссылкой на вакансию
        link_element = vacancy_list[i].find_element(
            By.CLASS_NAME, 'bloko-button')
        link = link_element.get_attribute('href')
        salary = link_element.get_attribute('salary')
        print(salary)
        company_name = link_element.get_attribute('company_name')
        print(company_name)
        city = link_element.get_attribute('city')
        print(city)
        content = vacancy_list[i].text
        # Добавление данных о вакансии в список
        parser_data.append({
            "Content": content,
            "Link": link,
            "Salary": salary,
            "Company_name": company_name,
            "City": city
            })
    except Exception as e:
        print(f"Не удалось найти ссылку для вакансии {i}: {e}")

    print(f"Вакансия {i} обработана")

print(f"Обработано {len(parser_data)} вакансий")


# Запись в файл обработанных вакансий, добавление новых в конец
def write_to_csv(data, filename):
    # Проверяем, существует ли файл
    file_exists = os.path.isfile(filename)

    # Открываем файл на запись или создаем новый,
    # если он не существует, иначе открываем на дозапись
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        # Если файл новый, добавляем заголовки
        if not file_exists:
            writer.writerow(['Numder', 'Content', 'Link'])

        # Записываем данные с нумерацией
        for i, item in enumerate(data, start=1):
            writer.writerow([i, item['Content'], item['Link']])


write_to_csv(parser_data, 'WEB-SCRAPING/vacancies_selenium.csv')
print('Данные записаны в файл "WEB-SCRAPING/vacancies_selenium.csv"')
print('-----------------------------')


browser.quit()
print('Браузер закрыт')
