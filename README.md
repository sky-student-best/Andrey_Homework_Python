# Andrey_Homework_Python
# Lesson 10: Page Object + Allure

Автотесты UI на Selenium с паттерном Page Object и отчётом Allure.

## Запуск тестов с формированием отчёта

1. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

2. Запустите тесты с сохранением результатов:

    ```bash
    pytest lesson_10 --alluredir=allure-results
    ```

3. Откройте отчёт:

    ```bash
    allure serve allure-results
    ```

Команда `allure serve` сгенерирует отчёт и откроет его в браузере.

## Что в отчёте

- Название и описание каждого теста (`@allure.title`, `@allure.description`).
- Группировка по функциональности (`@allure.feature`).
- Критичность теста (`@allure.severity`).
- Пошаговый ход выполнения (`with allure.step` и `@allure.step`).

## Структура

- `conftest.py` — фикстуры браузеров (Chrome, Firefox).
- `*_page.py` — классы Page Object с документацией.
- `test_*.py` — тесты с разметкой Allure.
