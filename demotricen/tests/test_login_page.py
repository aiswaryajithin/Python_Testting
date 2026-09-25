from demotricen.pages.login_page import LoginPage
from  selenium.webdriver import Chrome,ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)

def test_login():
    driver=Chrome(options=o)
    driver.get('https://demowebshop.tricentis.com/login')
    driver.maximize_window()
    sleep(2)

    login=LoginPage(driver)
    login.enter_username("aiswarya")
    login.enter_password("1234@abc")
    login.login_btn

    sleep(2)
    driver.quit()
