import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_calculator():
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.page_load_strategy = "eager"

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    wait = WebDriverWait(driver, 90)

    try:
        base_dir = Path(__file__).resolve().parent
        html_file = base_dir / "slow_calculator.html"
        file_url = html_file.as_uri()

        print(f"Открываем локальную страницу: {file_url}")
        driver.get(file_url)

        delay_input = wait.until(EC.visibility_of_element_located((By.ID, "delay")))
        start_btn = wait.until(EC.element_to_be_clickable((By.ID, "start")))

        delay_input.clear()
        delay_input.send_keys("45")
        start_btn.click()


        def result_changed(driver):
            el = driver.find_element(By.ID, "result")
            if el.is_displayed() and el.text.strip() != "Результат: —":
                return el
            return False

        result_element = wait.until(result_changed)

        result_text = result_element.text.strip()
        print("Результат калькулятора:", result_text)

        assert result_text.startswith("Результат: ")
        assert "90" in result_text or result_text == "Результат: 90", f"Ожидался 90, но получили: {result_text}"
        print("Тест пройден.")

    finally:
        driver.quit()
