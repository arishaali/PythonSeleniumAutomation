from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, browser):
        self.driver = browser
        self.username = (By.ID, "txt-username")
        self.password = (By.ID, "txt-password")
        self.login_btn = (By.ID, "btn-login")

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()
