from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver, timeout=90):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, value: str):
        delay_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys(value)

        try:
            self.wait.until(
                EC.invisibility_of_element_located(
                    (By.CSS_SELECTOR, ".loading-overlay")
                )
            )
        except Exception:
            import time
            time.sleep(2)

    def click_button(self, text: str):
        locator = f"//span[text()='{text}']"
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, locator)),
            message=f"Кнопка '{text}' не стала кликабельной"
        )
        element.click()

    def get_result_text(self) -> str:
        def is_numeric_result(driver):
            result_element = driver.find_element(By.CSS_SELECTOR, ".screen")
            text = result_element.text.strip()
            clean = text.replace(" ", "")
            if any(op in clean for op in ["+", "-", "*", "/"]):
                return False
            return clean.lstrip("-").isdigit()

        self.wait.until(
            is_numeric_result,
            message="Результат не стал числом за отведённое время"
        )

        result_element = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result_element.text.strip()
