from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Appointment:
    def __init__(self, browser):
        self.driver = browser
    
    def book_appointment(self, facility, readmission, program, visit_date, comment):
        #Facility Field
        facility_dropdown = Select(self.driver.find_element(By.ID, "combo_facility"))
        facility_dropdown.select_by_visible_text(facility)

        #Checkbox for apply for hospital readmission (optional)
        checkbox = self.driver.find_element(By.NAME, "hospital_readmission")
        if readmission and not checkbox.is_selected():
            checkbox.click()
        elif not readmission and checkbox.is_selected():
            checkbox.click()

        #Healthcare program radio button (By default first one is selected)
        program = program.lower()
        self.driver.find_element(By.ID, f"radio_program_{program}").click()

        #Datepicker
        self.driver.find_element(By.ID,'txt_visit_date').clear()
        self.driver.find_element(By.ID,'txt_visit_date').send_keys(visit_date)

        #Comment
        comment_box = self.driver.find_element(By.ID, "txt_comment")
        comment_box.clear()
        comment_box.send_keys(comment)

        #Click Book button
        self.driver.find_element(By.ID,"btn-book-appointment").click()



