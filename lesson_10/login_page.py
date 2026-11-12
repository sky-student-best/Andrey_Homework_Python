from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
    """Страница авторизации магазина saucedemo.com."""

    def __init__(self, driver: WebDriver, timeout: int = 60) -> None:
        """
        Инициализация страницы авторизации.

        :param driver: экземпляр WebDriver для управления браузером.
        :type driver: WebDriver
        :param timeout: время ожидания элементов в секундах.
        :type timeout: int
        :return: None
        :rtype: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.url = "https://www.saucedemo.com/"

    def open(self) -> None:
        """
        Открывает страницу авторизации.

        :return: None
        :rtype: None
        """
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        """
        Заполняет форму и выполняет вход в систему.

        :param username: логин пользователя.
        :type username: str
        :param password: пароль пользователя.
        :type password: str
        :return: None
        :rtype: None
        """
        username_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, "user-name")),
            message="Поле user-name не стало кликабельным"
        )
        username_input.clear()
        username_input.send_keys(username)

        password_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, "password")),
            message="Поле password не стало кликабельным"
        )
        password_input.clear()
        password_input.send_keys(password)

        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn_action")),
            message="Кнопка входа не стала кликабельной"
        )
        login_btn.click()

    def wait_for_inventory_page(self) -> None:
        """
        Ожидает перехода на страницу каталога товаров после входа.

        :return: None
        :rtype: None
        """
        self.wait.until(
            lambda d: d.current_url.startswith(
                "https://www.saucedemo.com/inventory.html"
            ),
            message="Не удалось перейти на страницу инвентаря"
        )
