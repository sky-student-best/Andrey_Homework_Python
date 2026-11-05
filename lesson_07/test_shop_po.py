import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    options = Options()
    options.page_load_strategy = "eager"
    options.add_argument("--disable-extensions")

    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()


def test_checkout_flow_with_page_objects(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    login_page.wait_for_inventory_page()

    products_to_add = {
        "Sauce Labs Backpack": "#add-to-cart-sauce-labs-backpack",
        "Sauce Labs Bolt T-Shirt": "#add-to-cart-sauce-labs-bolt-t-shirt",
        "Sauce Labs Onesie": "#add-to-cart-sauce-labs-onesie",
    }
    inventory_page.add_products_batch(products_to_add)

    cart_count = inventory_page.get_cart_badge_count()
    assert cart_count == 3, (
        f"Ожидалось 3 товара в корзине, а там: {cart_count}"
    )

    inventory_page.go_to_cart()
    cart_page.wait_for_cart_page()
    cart_page.proceed_to_checkout()

    checkout_page.fill_shipping_info("Andrey", "Testov", "12345")
    checkout_page.continue_checkout()
    checkout_page.wait_for_checkout_step_two()

    total_text = checkout_page.get_total_amount()
    expected_total = "$58.29"
    assert expected_total in total_text, (
        f"Ожидалось {expected_total}, но получено: {total_text}"
    )
