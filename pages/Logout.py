from selenium.webdriver.common.by import By

class Logout:
    def __init__(self, browser):
        self.driver = browser
    
    def logout(self):
        menu = self.driver.find_element(By.ID,"menu-toggle")
        menu.click()
        self.driver.find_element(By.XPATH,"//*[@id='sidebar-wrapper']/ul/li[5]/a").click()