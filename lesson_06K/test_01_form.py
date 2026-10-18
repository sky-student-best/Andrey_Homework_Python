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
    wait = WebDriverWait(driver, 20)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    wait.until(
        EC.visibility_of_element_located((By.NAME, "first-name"))
    ).send_keys("Иван")
    wait.until(
        EC.visibility_of_element_located((By.NAME, "last-name"))
    ).send_keys("Петров")
    wait.until(
        EC.visibility_of_element_located((By.NAME, "address"))
    ).send_keys("Ленина, 55")
    wait.until(
        EC.visibility_of_element_located((By.NAME, "city"))
    ).send_keys("Москва")
    wait.until(
        EC.visibility_of_element_located((By.NAME, "country"))
    ).send_keys("Россия")

    zip_input = wait.until(
        EC.visibility_of_element_located((By.NAME, "zip-code"))
    )
    zip_input.clear()

    email_input = wait.until(
        EC.visibility_of_element_located((By.NAME, "e-mail"))
    )
    email_input.send_keys("test@skypro.com")

    wait.until(
        EC.visibility_of_element_located((By.NAME, "phone"))
    ).send_keys("+79990000000")
    wait.until(
        EC.visibility_of_element_located((By.NAME, "job-position"))
    ).send_keys("QA")
    wait.until(
        EC.visibility_of_element_located((By.NAME, "company"))
    ).send_keys("SkyPro")

    submit_btn = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[type='submit'], button[type='submit']")
        )
    )
    submit_btn.click()

    wait.until(lambda d: "data-types-submitted.html" in d.current_url)
    body_text = driver.find_element(By.TAG_NAME, "body").text

    assert "Иван" in body_text
    assert "Петров" in body_text
    assert "Москва" in body_text
    assert "test@skypro.com" in body_text
