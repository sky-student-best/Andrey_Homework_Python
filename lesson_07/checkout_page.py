from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver, timeout=60):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_checkout_step_two(self):
        self.wait.until(
            lambda d: d.current_url.endswith("/checkout-step-two.html"),
            message="Не удалось перейти на шаг 2 оформления заказа"
        )

    def fill_shipping_info(
        self, first_name: str, last_name: str, zip_code: str
    ):
        first_name_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, "first-name")),
            message="Поле First Name не стало кликабельным"
        )
        first_name_input.clear()
        first_name_input.send_keys(first_name)

        last_name_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, "last-name")),
            message="Поле Last Name не стало кликабельным"
        )
        last_name_input.clear()
        last_name_input.send_keys(last_name)

        zip_code_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, "postal-code")),
            message="Поле Postal Code не стало кликабельным"
        )
        zip_code_input.clear()
        zip_code_input.send_keys(zip_code)

    def continue_checkout(self):
        continue_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart_button")),
            message="Кнопка Continue не стала кликабельной"
        )
        continue_btn.click()

    def get_total_amount(self) -> str:
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            ),
            message="Сумма заказа не найдена"
        )
        return total_element.text
