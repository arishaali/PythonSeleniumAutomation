from pages.Login_page import LoginPage
from pages.Logout import Logout
import pytest

@pytest.mark.login 
def test_valid_login(browser):
     
    """Test to verify valid login on CURA Healthcare website."""

    browser.get("https://katalon-demo-cura.herokuapp.com/")
    browser.maximize_window()
    browser.find_element("id", "btn-make-appointment").click()

    login = LoginPage(browser)
    login.login("John Doe", "ThisIsNotAPassword")

    assert "appointment" in browser.current_url, "Login failed or did not redirect properly."

@pytest.mark.login 
def test_invalid_login(browser):
     
    """Test to verify invalid login on CURA Healthcare website."""

    #Logout first because this test run in same session

    home=Logout(browser)
    home.logout()

    browser.get("https://katalon-demo-cura.herokuapp.com/")
    browser.maximize_window()
    browser.find_element("id", "btn-make-appointment").click()

    login = LoginPage(browser)
    login.login("InvalidUser", "InvalidPassword")

    assert "Login failed! Please ensure the username and password are valid." in browser.page_source



