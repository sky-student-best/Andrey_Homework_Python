from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")
    time.sleep(1)

    links = driver.find_elements(By.TAG_NAME, "a")
    time.sleep(1)

    assert len(links) == 9
    time.sleep(1)

    for link in links:
        assert link.is_displayed()
        time.sleep(1)

    assert "1" in links[0].text

    driver.quit()
