import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page import Page


class HomePage(Page):
    search_field = (By.XPATH, "//*[@id='root']/div/header/div[2]/div[1]/div/div/div/div/div[3]/input")

    def __init__(self, driver):
        super().__init__(driver)

    def search_item_by(self, keyword):
        self.set_value(self.search_field, keyword)
        self.get_element_by(self.search_field).send_keys(Keys.RETURN)
        return SearchResultPage(self.driver)


class SearchResultPage(Page):
    product_name = (By.LINK_TEXT, "Whoscall象卡來市話版 家中防詐神器（免服務年費與一年主機保固）")

    def __init__(self, driver):
        super().__init__(driver)

    def open_product_details_page(self):
        self.get_element_by(self.product_name).click()
        # because of open a new tab, we need to switch tab here
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        return ProductPage(self.driver)


class ProductPage(Page):
    product_price = (By.CLASS_NAME, "o-prodPrice__price")
    spec_title = (By.CLASS_NAME, "c-prodSpecs__info")

    def __init__(self, driver):
        super().__init__(driver)

    def get_product_price(self):
        return self.get_element_by(self.product_price).text

    def take_a_screenshot(self, filename):
        self.save_screen_shot(self.get_element_by(self.spec_title), "screenshot.png")
