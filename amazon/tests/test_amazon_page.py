from amazon.pages.amazon_page import SearchPage
from selenium import webdriver


def test_serach(setup_and_teardown):

    search=SearchPage(setup_and_teardown)
    search.enter_serachitem("perfumes")
    search.search_click()
    search.handle_dropdown("Price: High to Low")
    search.click_3rd_item()
    setup_and_teardown.switch_to.window(setup_and_teardown.window_handles[-1])
    search.add_to_cart()

