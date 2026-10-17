import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options

def test_form():
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    
    driver = webdriver.Edge(
        service=webdriver.EdgeService(EdgeChromiumDriverManager().install()),
        options=options
    )
    wait = WebDriverWait(driver, 60)

    try:
        base_dir = Path(__file__).resolve().parent  # папка lesson_06K
        html_file = base_dir / "form_test_page.html"
        
        file_url = html_file.as_uri()
        print(f"Открываем локальную страницу: {file_url}")
        driver.get(file_url)

        wait.until(lambda d: d.title and "Test Form Page" in d.title)

        wait.until(EC.visibility_of_element_located((By.NAME, "firstName"))).send_keys("Иван")
        driver.find_element(By.NAME, "lastName").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        
        zip_field = driver.find_element(By.NAME, "zipCode")
        zip_field.clear()  # Оставить пустым, как в задании
        
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "jobPosition").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        submit_btn = wait.until(EC.element_to_be_clickable((By.ID, "submitBtn")))
        submit_btn.click()

        zip_color = zip_field.value_of_css_property("border-color")
        first_name_color = driver.find_element(By.NAME, "firstName").value_of_css_property("border-color")

        print(f"Цвет Zip code: {zip_color}")
        print(f"Цвет First name: {first_name_color}")

        is_zip_red = ("red" in zip_color.lower()) or ("rgb(255" in zip_color)
        assert is_zip_red, f"Поле Zip code должно быть красным, но цвет: {zip_color}"

        is_first_green = ("green" in first_name_color.lower()) or ("rgb(0" in first_name_color)
        assert is_first_green, f"Остальные поля должны быть зелёными, но цвет первого поля: {first_name_color}"

        print("Тест пройден: валидация цветов подтверждена.")

    finally:
        driver.quit()
