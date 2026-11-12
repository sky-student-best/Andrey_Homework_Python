import allure

from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.title("Полный сценарий покупки трёх товаров в магазине")
@allure.description(
    "Пользователь авторизуется под standard_user, добавляет в корзину "
    "три товара, переходит в корзину, оформляет заказ и проверяет "
    "итоговую сумму на шаге 2 оформления."
)
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_checkout_flow_with_page_objects(firefox_driver):
    """Сквозной сценарий: логин, корзина, оформление заказа."""
    login_page = LoginPage(firefox_driver)
    inventory_page = InventoryPage(firefox_driver)
    cart_page = CartPage(firefox_driver)
    checkout_page = CheckoutPage(firefox_driver)

    with allure.step("Авторизоваться под standard_user"):
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        login_page.wait_for_inventory_page()

    with allure.step("Добавить в корзину три товара"):
        products_to_add = {
            "Sauce Labs Backpack":
                "#add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt":
                "#add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Onesie":
                "#add-to-cart-sauce-labs-onesie",
        }
        inventory_page.add_products_batch(products_to_add)

    with allure.step("Проверить счётчик корзины"):
        cart_count = inventory_page.get_cart_badge_count()
        assert cart_count == 3, (
            f"Ожидалось 3 товара в корзине, а там: {cart_count}"
        )

    with allure.step("Перейти в корзину и начать оформление"):
        inventory_page.go_to_cart()
        cart_page.wait_for_cart_page()
        cart_page.proceed_to_checkout()

    with allure.step("Заполнить данные покупателя и продолжить"):
        checkout_page.fill_shipping_info("Andrey", "Testov", "12345")
        checkout_page.continue_checkout()
        checkout_page.wait_for_checkout_step_two()

    with allure.step("Проверить итоговую сумму заказа"):
        total_text = checkout_page.get_total_amount()
        expected_total = "$58.29"
        assert expected_total in total_text, (
            f"Ожидалось {expected_total}, но получено: {total_text}"
        )
