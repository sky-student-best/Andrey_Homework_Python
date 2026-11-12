import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Страница калькулятора с медленным откликом."""

    def __init__(self, driver: WebDriver, timeout: int = 60) -> None:
        """
        Инициализация страницы калькулятора.

        :param driver: экземпляр WebDriver для управления браузером.
        :type driver: WebDriver
        :param timeout: время ожидания элементов в секундах.
        :type timeout: int
        :return: None
        :rtype: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        :return: None
        :rtype: None
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, value: str) -> None:
        """
        Вводит значение в поле задержки вычислений.

        :param value: задержка в секундах, например "45".
        :type value: str
        :return: None
        :rtype: None
        """
        field = self.driver.find_element(By.ID, "delay")
        field.clear()
        field.send_keys(value)

    def click_button(self, button: str) -> None:
        """
        Нажимает кнопку калькулятора по её тексту.

        :param button: текст кнопки, например "7", "+", "=".
        :type button: str
        :return: None
        :rtype: None
        """
        btn = self.wait.until(EC.element_to_be_clickable((
            By.XPATH,
            f"//span[text()='{button}']",
        )))
        btn.click()

    def get_result_text(self) -> str:
        """
        Возвращает текст из поля результата.

        :return: текущее значение на экране калькулятора.
        :rtype: str
        """
        screen = self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "screen")
        ))
        return screen.text
