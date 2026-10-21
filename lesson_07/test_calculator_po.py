import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_calculator_with_page_object(driver):
    page = CalculatorPage(driver)
    page.open()
    page.set_delay("45")

    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    result = page.get_result_text()
    assert result == "15", f"Ожидался результат 15, но было: {result}"
