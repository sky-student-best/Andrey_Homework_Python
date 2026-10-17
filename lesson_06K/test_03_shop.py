from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkout_flow():
    options = Options()
    options.page_load_strategy = "eager"

    driver = None
    try:
        driver = webdriver.Firefox(options=options)
        wait = WebDriverWait(driver, 60)

        driver.get("https://www.saucedemo.com/")

        username_input = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username_input.send_keys("standard_user")

        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")

        login_btn = driver.find_element(By.CLASS_NAME, "btn_action")
        login_btn.click()

        wait.until(
            lambda d: d.current_url.startswith("https://www.saucedemo.com/inventory.html")
        )

        products_to_add = {
            "Sauce Labs Backpack": "#add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt": "#add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Onesie": "#add-to-cart-sauce-labs-onesie"
        }

        for product_name, button_id in products_to_add.items():
            product_elem = wait.until(
                lambda d: d.find_element(
                    By.XPATH,
                    f"//div[@class='inventory_item']//div[contains(text(), '{product_name}')]"
                )
            )
            print(f"Товар '{product_name}' найден.")

            add_btn = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, button_id)),
                message=f"Кнопка не найдена по ID {button_id} для товара {product_name}"
            )

            add_btn.click()
            print(f'Клик по кнопке "Add to cart". Товар добавлен.')

        cart_badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        assert int(cart_badge.text) == 3, f"Ожидалось 3 товара в корзине, а там: {cart_badge.text}"
        print("В корзине 3 товара. Переходим к оформлению...")

        cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_container")
        cart_link.click()

        wait.until(lambda d: d.current_url.endswith("/cart.html"))
        print("Страница корзины загружена.")

        checkout_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout")),
            message="Кнопка Checkout не найдена по ID #checkout"
        )
        checkout_btn.click()
        print("Нажали Checkout по ID #checkout.")

        first_name_input = wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        first_name_input.send_keys("Andrey")

        last_name_input = driver.find_element(By.ID, "last-name")
        last_name_input.send_keys("Testov")

        zip_code_input = driver.find_element(By.ID, "postal-code")
        zip_code_input.send_keys("12345")

        continue_btn = driver.find_element(By.CSS_SELECTOR, ".cart_button")
        continue_btn.click()

        wait.until(lambda d: d.current_url.endswith("/checkout-step-two.html"))

        total_element = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        print(f"Итоговая стоимость: {total_text}")

        expected_total = "$58.29"
        if expected_total in total_text:
            print("✅ Итоговая сумма совпадает: $58.29")
        else:
            raise AssertionError(f"Ожидалось {expected_total}, но получено: {total_text}")

        print("Тест checkout_flow: ПРОЙДЕН ✅")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise
    finally:
        if driver is not None:
            driver.quit()
