from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver, timeout=60):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.url = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.url)

    def login(self, username: str, password: str):
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

    def wait_for_inventory_page(self):
        self.wait.until(
            lambda d: d.current_url.startswith(
                "https://www.saucedemo.com/inventory.html"
            ),
            message="Не удалось перейти на страницу инвентаря"
        )
