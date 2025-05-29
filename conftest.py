# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Shared browser (faster, for most tests)
@pytest.fixture(scope="module")
def browser():
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        yield driver
        driver.quit()
    except Exception as e:
        print(f"Error during fixture setup: {e}")
        raise

# Fresh browser (isolated, for specific tests)
@pytest.fixture(scope="function")
def fresh_browser():
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        yield driver
        driver.quit()
    except Exception as e:
        print(f"Error during fixture setup: {e}")
        raise