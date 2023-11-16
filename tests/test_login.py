import configparser
import time
import unittest
from time import sleep

from selenium import webdriver

from login import HomePage


class TestAuthentication(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://24h.pchome.com.tw/")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_check_the_product_price_successfully(self):
        keyword = "whoscall"
        page = HomePage(self.driver).search_item_by(keyword).open_product_details_page()

        # check the product price
        result = page.get_product_price()
        expected = "$999"
        self.assertEqual(result, expected)

        # take a screenshot
        page.take_a_screenshot("screenshot.png")


if __name__ == '__main__':
    unittest.main()
