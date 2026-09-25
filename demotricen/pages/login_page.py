from selenium.webdriver.common.by import By

class LoginPage:
    username=(By.ID,'Email')
    password=(By.ID,'Password')
    login_btn=(By.XPATH,'//input[@value="Log in"]')

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,username):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()
