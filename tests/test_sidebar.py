from selenium.webdriver.common.by import By
import pytest
from pages.Login_page import LoginPage

def test_hamburger_menu_displayed(browser):
    browser.get("https://katalon-demo-cura.herokuapp.com/")

    browser.find_element(By.ID,"menu-toggle").click()
    sidebar=browser.find_element(By.ID,"sidebar-wrapper")
    assert sidebar.is_displayed()

def test_sidebar_links_exist_before_login(browser):
    browser.get("https://katalon-demo-cura.herokuapp.com/")
    browser.find_element(By.ID,"menu-toggle").click()
    browser.find_element(By.ID,"sidebar-wrapper")
    expected_links = ["Home", "Login"]

    for link in expected_links:
        link_text = browser.find_element(By.LINK_TEXT,link)
        assert link_text.is_displayed(), f"{link_text} not in sidebar"

@pytest.mark.parametrize("link_text, expected_in_page", [
    ("Home", "CURA Healthcare Service"),
    ("Login", "Login")
])
def test_sidebar_links_navigation_before_login(browser, link_text, expected_in_page):
    browser.get("https://katalon-demo-cura.herokuapp.com/")
    browser.find_element(By.ID, "menu-toggle").click()
    
    browser.find_element(By.LINK_TEXT, link_text).click()

    assert expected_in_page in browser.page_source

def test_sidebar_links_exist_after_login(browser):
    browser.get("https://katalon-demo-cura.herokuapp.com/")
    browser.find_element("id", "btn-make-appointment").click()

    login = LoginPage(browser)
    login.login("John Doe", "ThisIsNotAPassword")

    browser.find_element(By.ID,"menu-toggle").click()
    browser.find_element(By.ID,"sidebar-wrapper")
    expected_links = ["Home", "History", "Profile", "Logout"]

    for link in expected_links:
        link_text = browser.find_element(By.LINK_TEXT,link)
        assert link_text.is_displayed(), f"{link_text} not in sidebar"

# @pytest.mark.parametrize("link_text, expected_in_page", [
#     ("Home", "CURA Healthcare Service"),
#     ("History", "History"),
#     ("Profile", "Profile"),
#     ("Logout", "CURA Healthcare Service"),
# ])
# def test_sidebar_links_navigation_after_login(browser, link_text, expected_in_page):
#     browser.get("https://katalon-demo-cura.herokuapp.com/")
#     browser.find_element(By.ID, "btn-make-appointment").click()

#     login = LoginPage(browser)
#     login.login("John Doe", "ThisIsNotAPassword")

#     browser.find_element(By.ID, "menu-toggle").click()
#     browser.find_element(By.LINK_TEXT, link_text).click()

#     assert expected_in_page in browser.page_source




