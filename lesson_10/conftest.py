import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def chrome_driver():
    """Фикстура с Chrome. После теста браузер закрывается."""
    options = ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    """Фикстура с Firefox (стратегия eager). Закрывается после теста."""
    options = FirefoxOptions()
    options.page_load_strategy = "eager"
    options.add_argument("--disable-extensions")

    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()
