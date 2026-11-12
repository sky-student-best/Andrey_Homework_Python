from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartPage:
    """Страница корзины магазина."""

    def __init__(self, driver: WebDriver, timeout: int = 60) -> None:
        """
        Инициализация страницы корзины.

        :param driver: экземпляр WebDriver для управления браузером.
        :type driver: WebDriver
        :param timeout: время ожидания элементов в секундах.
        :type timeout: int
        :return: None
        :rtype: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_cart_page(self) -> None:
        """
        Ожидает загрузки страницы корзины.

        :return: None
        :rtype: None
        """
        self.wait.until(
            lambda d: d.current_url.endswith("/cart.html"),
            message="Не удалось загрузить страницу корзины"
        )

    def proceed_to_checkout(self) -> None:
        """
        Нажимает кнопку перехода к оформлению заказа.

        :return: None
        :rtype: None
        """
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout")),
            message="Кнопка Checkout не найдена"
        )
        checkout_btn.click()
