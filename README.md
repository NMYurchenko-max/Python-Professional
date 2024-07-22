## Привет, меня зовут Нина. Я изучаю Python online на образовательной платформе "НЕТОЛОГИЯ"

### Это мой учебный репозиторий для выполнения заданий по модулю "Профессиональная работа с Python".

Он содержит выполненный мной код по темам изучения

_____

### Структура (будет пополняься по мере изучения)
================================

### [Тема 1: "Модули, пакеты, импорты в Python":](/Import_Modules_Package/)
- [Презентация](/Import_Modules_Package/Презентация_Модули__пакеты__импорты_в_Python.pdf)

- [Задание:](https://github.com/netology-code/py-homeworks-advanced/tree/master/1.Import.Module.Package)

#####  Исполнение:

- [main.py - Пакет "Бухгалтерия"](/Import_Modules_Package/bookkeeping/main.py)

##### Примеры освоения модулей из Pypi (много интересного). Немного познакомилась использовала в реализации медиаплеера. Воспроизводит фото разных форматов, ауди и видео файлы:
  
- [Медиаплеер](/Import_Modules_Package/media/v1.3._mtdia_player.py)

##### Файл зависимостей записан командой (его содержание относится ко всему репозиторию)
```
pip freeze > requirements.txt
```
  
- [Файл requirements.txt](/requirements.txt)


================================

### [Тема 2: "Регулярные выражения:"](/Regulars/)
- [Презентация](/Regulars/Преентаци_-_Регулярные_выражения_78.pdf)
- [Задание](https://github.com/netology-code/py-homeworks-advanced/blob/master/5.Regexp/README.md)
- [Приложение 'regular expressions'](https://regex101.com/)
  
- [Документация Python3.12.4. Modul re](https://docs.python.org/3/library/re.html)

 #####  Исполнение:
- [main.py](/Regulars/main.py) - удачная реализация

- [normalize.py](/Regulars/normalize.py)  - неудачная реализация (по стопам лекции)

=================================
### [Тема 3: WEB-SCRAPING:](/WEB-SCRAPING/)

- [Презентация](/WEB-SCRAPING/Present_Веб-скрапинг_Табельский.pdf)
  
- [Задание](https://github.com/netology-code/py-homeworks-advanced/tree/new_hw_scrapping/6.Web-scrapping)
  
- Исполнение, варианты:
   1. [Использован Selenium](WEB-SCRAPING/selenium_test.py)- позволил получить всю информацию, текст в разрезе отдельной вакансии: 

   * [Результат](WEB-SCRAPING/vacancies_selenium.csv)
   
   2. [Использован requests + BeautifulSoup](WEB-SCRAPING/main2.py) - текст в разрезе отдельной вакансии, в 2-х вариантах, загрузить зарплату и город не удалось
   *  [вариант ч/з 'class_block'](/WEB-SCRAPING/main2.py) - использование классов блоков
      * [Результат](/WEB-SCRAPING/vacancies.csv)
   *  [вариант ч/з 'data-qa'](/WEB-SCRAPING//my_hh_parser.py) - использование
   атрибутов 'data-qa'
      * [Результат](WEB-SCRAPING/vacancies.json)
-  Для решения проблем с правильностью применения селекторов написала скрипт запроса к коду страницы парсинга, однако удачно запустить не удалось - ошибка доступности сайта
   * [скрипт](WEB-SCRAPING/feetch_tag.py) - прошу посмотреть что изменить чтобы скрипт запустить, проэкспериментировать...
  
#### Возможно я сама себе усложняю задачу, но хотелось бы все-таки понять какие селекторы применять, так как я опробовала все, и причины несрабатывания кода не понимаю!
=================================

### [Тема 4. Интеграторы и Генераторы:](/Iterators&Generators/)

- [Презентация](/Iterators&Generators/Present_Итераторы._Генераторы._Yield_3.11.22.pdf)

- [Задание](https://github.com/netology-code/py-homeworks-advanced/tree/master/2.Iterators.Generators.Yield)
- Исполнение
  * [Test-задание1](/Iterators&Generators/flat_iter_1.py)
  * [Test-Задание2](/Iterators&Generators//flat_gen_2.py)
  * [Test-Задание3](/Iterators&Generators/flat_iter_3.py)
  * [Test-Задание4](/Iterators&Generators/flat_gen_4.py)


=================================

### [Тема 5. Декораторы](/Decorators)
- [Презентация](/WEB-SCRAPING/Present_WEB-SCRAPE_3.11.22.pdf)
  
- [Задание](https://github.com/netology-code/py-homeworks-advanced/tree/master/3.Decorators)
  
- Исполнение
  * [Test-задание1](/Decorators/first_loger.py)
  * [Test-задание2](/Decorators/path_loger.py)
  * [Применить написанный логгер к приложению из любого из предыдущих заданий. Результат применения](/Decorators/my_log.log)
    * [Написанный логгер](/Decorators/logging_decorator.py)
    * [Скрипт скрапинга hh.ru](/Decorators/hh_scraping_log.py)

=================================

[РЕПОЗИТОРИЙ НЕТОЛОГИИ -ДЗ](
https://github.com/netology-code/py-homeworks-advanced/blob/master)
