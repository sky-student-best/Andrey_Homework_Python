from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class InventoryPage:
    """Страница каталога товаров магазина."""

    def __init__(self, driver: WebDriver, timeout: int = 60) -> None:
        """
        Инициализация страницы каталога.

        :param driver: экземпляр WebDriver для управления браузером.
        :type driver: WebDriver
        :param timeout: время ожидания элементов в секундах.
        :type timeout: int
        :return: None
        :rtype: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def _wait_for_product_visible(
        self, product_name: str
    ) -> object:
        """
        Ожидает видимости карточки товара по его названию.

        :param product_name: название товара на карточке.
        :type product_name: str
        :return: найденный элемент карточки товара.
        :rtype: object
        """
        locator = (
            By.XPATH,
            f"//div[@class='inventory_item']"
            f"//div[contains(text(), '{product_name}')]"
        )
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Товар '{product_name}' не найден на странице"
        )

    def add_product_by_id(self, button_id: str) -> None:
        """
        Добавляет товар в корзину по css-селектору кнопки.

        :param button_id: css-селектор кнопки добавления в корзину.
        :type button_id: str
        :return: None
        :rtype: None
        """
        locator = (By.CSS_SELECTOR, button_id)
        add_btn = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Кнопка не найдена по селектору {button_id}"
        )
        add_btn.click()

    def add_products_batch(
        self, products: dict[str, str]
    ) -> None:
        """
        Добавляет в корзину группу товаров из словаря.

        :param products: словарь
            {название товара: селектор кнопки добавления}.
        :type products: dict[str, str]
        :return: None
        :rtype: None
        """
        for product_name, button_id in products.items():
            self._wait_for_product_visible(product_name)
            self.add_product_by_id(button_id)

    def get_cart_badge_count(self) -> int:
        """
        Возвращает количество товаров на счётчике корзины.

        :return: число товаров рядом с иконкой корзины.
        :rtype: int
        """
        badge = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            ),
            message="Бейдж корзины не найден"
        )
        return int(badge.text)

    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины по клику на иконку корзины.

        :return: None
        :rtype: None
        """
        cart_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_container")
            ),
            message="Ссылка на корзину не стала кликабельной"
        )
        cart_link.click()
