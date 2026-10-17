from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_loading():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 90)  # Увеличили таймаут, чтобы дать сайту время

    try:
        # Требование: страница /2
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
        print("Страница запрошена.")

        start_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button"))
        )
        print("Кнопка найдена.")

        # Клик через JS — самый надёжный способ
        driver.execute_script("arguments[0].click();", start_button)
        print("Клик выполнен.")

        # Требование: ждём появления текста в элементе с id="finish"
        result_element = wait.until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )

        actual_text = result_element.text
        print(f"Найденный текст: '{actual_text}'")

        # Требование: проверяем, что текст равен "Hello World!"
        assert actual_text == "Hello World!", f"Ожидался 'Hello World!', но было: '{actual_text}'"

        driver.save_screenshot("dynamic_loading_success.png")
        print("Скриншот сохранён.")

    except Exception as e:
        driver.save_screenshot("dynamic_loading_failure.png")
        raise e
    finally:
        driver.quit()
