import pytest
from selenium import webdriver

@pytest.fixture(params=['chrome','firefox','edge'])
def setup_and_teardown(request):
    parameter=request.param
    if parameter=='chrome':
         driver=webdriver.Chrome()
    elif parameter=='firefox':
         driver=webdriver.Firefox()
    elif parameter=='edge':
         driver=webdriver.Edge()

    driver.get('https://www.amazon.in/')
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

