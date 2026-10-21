from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver, timeout=60):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_cart_page(self):
        self.wait.until(
            lambda d: d.current_url.endswith("/cart.html"),
            message="Не удалось загрузить страницу корзины"
        )

    def proceed_to_checkout(self):
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout")),
            message="Кнопка Checkout не найдена"
        )
        checkout_btn.click()
