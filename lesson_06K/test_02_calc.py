from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def test_calculator():
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")

    driver = None
    try:
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
        wait = WebDriverWait(driver, 90)

        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        delay_input = wait.until(
            EC.visibility_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys("45")

        # Кнопки — это span, ищем по тексту
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        result_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".screen"))
        )

        # Ждём, пока текст станет "15"
        wait.until(lambda d: result_element.text == "15")

        assert result_element.text == "15", (
            f"Ожидался результат 15, но было: {result_element.text}"
        )

    finally:
        if driver is not None:
            driver.quit()
