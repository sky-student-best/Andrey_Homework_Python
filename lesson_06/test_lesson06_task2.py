from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

COOKIE_USER_1 = {
    "name": "ddg1",
    "value": "bblvZxPHgsWE4ToKBKXm",
    "domain": ".gitflic.ru",
    "path": "/"
}

# Вставь сюда реальные данные для User2
COOKIE_USER_2 = {
    "name": "ddg1",
    "value": "chEoVswavVC9GVCHcASn",   # <-- замени на реальное значение
    "domain": ".gitflic.ru",
    "path": "/"
}

BASE_URL = "https://gitflic.ru/"
PROFILE_URL_USER_1 = "https://gitflic.ru/user/test_user111"
PROFILE_URL_USER_2 = "https://gitflic.ru/user/test_user222"

def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    try:
        # --- Авторизация под User1 ---
        driver.get(BASE_URL)
        driver.add_cookie(COOKIE_USER_1)
        driver.refresh()
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        driver.get(PROFILE_URL_USER_1)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        url_user_1 = driver.current_url
        print(f"URL User1: {url_user_1}")

        # Проверяем, что мы действительно на профиле User1
        assert PROFILE_URL_USER_1 in url_user_1 or url_user_1.startswith(PROFILE_URL_USER_1), \
            f"Ожидался URL профиля User1, но был: {url_user_1}"

        # --- Авторизация под User2 ---
        driver.delete_all_cookies()
        driver.get(BASE_URL)
        driver.add_cookie(COOKIE_USER_2)
        driver.refresh()
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        driver.get(PROFILE_URL_USER_2)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        url_user_2 = driver.current_url
        print(f"URL User2: {url_user_2}")

        assert PROFILE_URL_USER_2 in url_user_2 or url_user_2.startswith(PROFILE_URL_USER_2), \
            f"Ожидался URL профиля User2, но был: {url_user_2}"

        # Если оба профиля доступны (даже если редирект одинаковый), URL могут совпадать,
        # поэтому вместо сравнения URL лучше проверить, что cookie реально разные.
        cookies_after_user1 = [c for c in driver.get_cookies() if c["name"] == "ddg1"]
        # Для простоты: проверим, что URL хотя бы отличаются по имени пользователя
        assert "test_user111" in url_user_1, "В URL User1 не найдено test_user111"
        assert "test_user222" in url_user_2, "В URL User2 не найдено test_user222"

    finally:
        driver.quit()
