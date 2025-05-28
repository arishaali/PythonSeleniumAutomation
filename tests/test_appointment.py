from pages.Appointment_page import Appointment
from pages.Login_page import LoginPage
import pytest
from selenium.webdriver.common.by import By

def test_submit_valid_form(browser):
    browser.get("https://katalon-demo-cura.herokuapp.com/")
    browser.maximize_window()
    browser.find_element("id", "btn-make-appointment").click()

    login = LoginPage(browser)
    login.login("John Doe", "ThisIsNotAPassword")

    appointment=Appointment(browser)
    appointment.book_appointment(
        facility="Seoul CURA Healthcare Center", 
        readmission=True, 
        program="None", 
        visit_date="05/06/2025", 
        comment="Book my appointment.")

    assert "Appointment Confirmation" in browser.page_source

def test_submit_with_leaving_date_empty(browser):
    browser.find_element("id", "btn-make-appointment").click()
    appointment=Appointment(browser)
    appointment.book_appointment(
        facility="Seoul CURA Healthcare Center", 
        readmission=True, 
        program="None", 
        visit_date="", 
        comment="Book my appointment.")
    
    assert "Appointment Confirmation" not in browser.page_source

def test_appointment_data_on_confirmation_page(browser):

    browser.find_element("id", "btn-make-appointment").click()
    appointment=Appointment(browser)
    appointment.book_appointment(
        facility="Seoul CURA Healthcare Center", 
        readmission=True, 
        program="Medicare", 
        visit_date="05/06/2025", 
        comment="Book my appointment.")

    assert browser.find_element(By.ID,"facility").text == "Seoul CURA Healthcare Center"
    assert browser.find_element(By.ID,"program").text == "Medicare"
    assert browser.find_element(By.ID,"visit_date").text == "05/06/2025"
    assert browser.find_element(By.ID,"comment").text == "Book my appointment."
    assert browser.find_element(By.ID,"hospital_readmission").text == "Yes"

def test_without_comment(browser):
    browser.find_element("id", "btn-make-appointment").click()
    appointment=Appointment(browser)
    appointment.book_appointment(
        facility="Seoul CURA Healthcare Center", 
        readmission=True, 
        program="None", 
        visit_date="22/06/2025", 
        comment="")
    
    assert "Appointment Confirmation" in browser.page_source

@pytest.mark.xfail(reason="No frontend validation for date format on CURA site")
def test_invalid_date_format(browser):
    browser.find_element("id", "btn-make-appointment").click()
    appointment=Appointment(browser)
    appointment.book_appointment(
        facility="Seoul CURA Healthcare Center", 
        readmission=True, 
        program="None", 
        visit_date="99/99/9999", 
        comment="")
    
    assert "Appointment Confirmation" not in browser.page_source
# Note: Application allows invalid date format.
# This test is expected to fail until validation is implemented.

def test_logout_from_appointment_page(browser):
    browser.find_element(By.ID,"menu-toggle").click()
    browser.find_element(By.XPATH,"//*[@id='sidebar-wrapper']/ul/li[5]/a").click()

    # Assertion: back to homepage 
    assert "CURA Healthcare Service" in browser.page_source

