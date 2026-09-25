from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Actions:

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def click(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self,locator,text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def selection(self,locator,text):
        dropdown=self.driver.find_element(*locator)
        option=Select(dropdown)
        option.select_by_visible_text(text)



