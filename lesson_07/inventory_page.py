from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver, timeout=60):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def _wait_for_product_visible(self, product_name: str):
        locator = (
            By.XPATH,
            f"//div[@class='inventory_item']"
            f"//div[contains(text(), '{product_name}')]"
        )
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Товар '{product_name}' не найден на странице"
        )

    def add_product_by_id(self, button_id: str):
        locator = (By.CSS_SELECTOR, button_id)
        add_btn = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Кнопка не найдена по селектору {button_id}"
        )
        add_btn.click()

    def add_products_batch(self, products: dict[str, str]):
        for product_name, button_id in products.items():
            self._wait_for_product_visible(product_name)
            self.add_product_by_id(button_id)

    def get_cart_badge_count(self) -> int:
        badge = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            ),
            message="Бейдж корзины не найден"
        )
        return int(badge.text)

    def go_to_cart(self):
        cart_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_container")
            ),
            message="Ссылка на корзину не стала кликабельной"
        )
        cart_link.click()
