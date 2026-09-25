from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Actions:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def click(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def clear(self,locator):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()

    def send_keys(self,locator,value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    def auto_suggestion(self,locator,value):
        self.wait.until(EC.visibility_of_all_elements_located(locator))
        ele=self.driver.find_elements(*locator)
        for i in ele:
           # print(i.text)
            if value.lower() in i.text.lower():
                i.click()
                break

    def date_selection(self,locator,date_value):
        self.wait.until(EC.visibility_of_element_located(locator)).click()
        date_locator=self.find_element(By.Xpath,f'//abbr[@aria-label="{date_value}"]')
        self.wait.until(EC.visibility_of_element_located(date_locator)).click()

    def handling_iframe(self,locator,locator_close):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            ifra=self.driver.find_element(*locator)
            self.driver.switch_to.frame(ifra)
            self.wait.until(EC.element_to_be_clickable(locator_close)).click()
            self.driver.switch_to.default_content()
        except:
            self.driver.switch_to.default_content()