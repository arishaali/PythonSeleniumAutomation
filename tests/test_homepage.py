from selenium.webdriver.common.by import By

def test_homepage_loads(browser):
    browser.get("https://katalon-demo-cura.herokuapp.com/")
    assert "CURA Healthcare Service" in browser.title

def test_homepage_title(browser):
    browser.get("https://katalon-demo-cura.herokuapp.com/")
    browser.maximize_window()
    assert browser.title == "CURA Healthcare Service"

def test_make_appointment_button(browser):
    browser.get("https://katalon-demo-cura.herokuapp.com/")
    browser.maximize_window()
    btn=browser.find_element("id", "btn-make-appointment")
    assert btn.is_displayed()
    btn.click()
    assert "Login" in browser.page_source 

def test_hamburger_menu_toggle(browser):
    browser.get("https://katalon-demo-cura.herokuapp.com/")

    browser.find_element(By.ID,"menu-toggle").click()
    sidebar=browser.find_element(By.ID,"sidebar-wrapper")
    assert sidebar.is_displayed()


