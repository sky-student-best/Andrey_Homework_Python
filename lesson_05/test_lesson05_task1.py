from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")
    time.sleep(3)

    html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_form_link.click()
    time.sleep(3)

    assert "/forms/post" in driver.current_url

    driver.back()
    time.sleep(3)

    assert driver.current_url == "https://httpbin.qa-territory.online/"

    driver.quit()
