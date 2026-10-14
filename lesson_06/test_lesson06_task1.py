from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_loading():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    # Никаких user-data-dir и sandbox

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 60)

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        print("Страница запрошена.")

        start_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button"))
        )
        print("Кнопка найдена.")

        # Клик через JS — самый надёжный
        driver.execute_script("arguments[0].click();", start_button)
        print("Клик выполнен.")

        # ВАЖНО: ждём появления лоадера (он есть всегда, если JS хоть чуть-чуть сработал)
        loader = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".example-loader"))
        )
        assert loader.is_displayed(), "Лоадер должен появиться после клика"
        print("Лоадер виден — динамика работает.")

        driver.save_screenshot("dynamic_loading_loader.png")
        print("Скриншот сохранён.")

    except Exception as e:
        driver.save_screenshot("dynamic_loading_failure.png")
        raise e
    finally:
        driver.quit()
