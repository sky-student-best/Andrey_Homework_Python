from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CheckoutPage:
    """Страница оформления заказа (шаги 1 и 2)."""

    def __init__(self, driver: WebDriver, timeout: int = 60) -> None:
        """
        Инициализация страницы оформления заказа.

        :param driver: экземпляр WebDriver для управления браузером.
        :type driver: WebDriver
        :param timeout: время ожидания элементов в секундах.
        :type timeout: int
        :return: None
        :rtype: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_checkout_step_two(self) -> None:
        """
        Ожидает перехода на второй шаг оформления заказа.

        :return: None
        :rtype: None
        """
        self.wait.until(
            lambda d: d.current_url.endswith("/checkout-step-two.html"),
            message="Не удалось перейти на шаг 2 оформления заказа"
        )

    def fill_shipping_info(
        self, first_name: str, last_name: str, zip_code: str
    ) -> None:
        """
        Заполняет данные покупателя на первом шаге оформления.

        :param first_name: имя покупателя.
        :type first_name: str
        :param last_name: фамилия покупателя.
        :type last_name: str
        :param zip_code: почтовый индекс покупателя.
        :type zip_code: str
        :return: None
        :rtype: None
        """
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

    def continue_checkout(self) -> None:
        """
        Нажимает кнопку Continue и переходит ко второму шагу.

        :return: None
        :rtype: None
        """
        continue_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart_button")),
            message="Кнопка Continue не стала кликабельной"
        )
        continue_btn.click()

    def get_total_amount(self) -> str:
        """
        Возвращает итоговую сумму заказа из сводки.

        :return: строка с итоговой суммой, например "Total: $58.29".
        :rtype: str
        """
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            ),
            message="Сумма заказа не найдена"
        )
        return total_element.text
