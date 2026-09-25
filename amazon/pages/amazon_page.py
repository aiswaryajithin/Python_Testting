from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from amazon.pages.base_page import Actions


class SearchPage(Actions):
    search_item=(By.ID,'twotabsearchtextbox')
    search_btn=(By.ID,'nav-search-submit-button')
    drop_down=(By.XPATH,'//select[@data-action="a-dropdown-select"]')
    item=(By.XPATH,'(//div[@class="a-section aok-relative s-image-square-aspect"])[3]')
    add_cart=(By.XPATH,'//input[@id="add-to-cart-button"]')

    def enter_serachitem(self,search_value):
        self.send_keys(self.search_item,search_value)

    def search_click(self):
       self.click(self.search_btn)

    def handle_dropdown(self,option):
        self.selection(self.drop_down,option)

    def click_3rd_item(self):
        self.click(self.item)

    def add_to_cart(self):

        self.click(self.add_cart)





