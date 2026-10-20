import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.EdgeOptions()
    service = EdgeService()
    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()


def test_form_validation(driver):
    wait = WebDriverWait(driver, 15)
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    fields_to_fill = [
        ("first-name", "Иван"),
        ("last-name", "Петров"),
        ("address", "Ленина, 55"),
        ("city", "Москва"),
        ("country", "Россия"),
        ("e-mail", "test@skypro.com"),
        ("phone", "+79990000000"),
        ("job-position", "QA"),
        ("company", "SkyPro"),
    ]

    for name, value in fields_to_fill:
        element = wait.until(
            EC.visibility_of_element_located((By.NAME, name))
        )
        element.send_keys(value)

    zip_input = wait.until(
        EC.visibility_of_element_located((By.NAME, "zip-code"))
        )
    zip_input.clear()

    submit_btn = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit'], input[type='submit']")
        )
    )
    submit_btn.click()

    zip_block = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    assert "alert-danger" in zip_block.get_attribute("class")

    first_name_block = wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    assert "alert-success" in first_name_block.get_attribute("class")

    wait.until(lambda d: "data-types-submitted.html" in d.current_url)

    body_text = driver.find_element(By.TAG_NAME, "body").text

    assert "Иван" in body_text
    assert "Петров" in body_text
    assert "Москва" in body_text
    assert "test@skypro.com" in body_text
