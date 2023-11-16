from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class Page:
    def __init__(self, driver):
        self.driver = driver

    def set_value(self, locator, value):
        elem = self.get_element_by(locator)
        # force focus on element before send_keys
        elem.click()
        if elem.tag_name == 'select':
            Select(elem).select_by_value(value)
        elif elem.get_attribute('type') == 'checkbox':
            elem.click()
        else:
            elem.clear()
            elem.send_keys(value)

    def get_element_by(self, by, timeout=10):
        """ Get element and wait it shows up """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(by)
            )
        except (NoSuchElementException, TimeoutException) as err:
            print(f"Exception Type: {type(err)}")
            raise
        return element

    def wait_for_visible(self, locator, timeout=10):
        """ Check the element if it is visible """
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(locator)
            )
        except (NoSuchElementException, TimeoutException) as err:
            print(f"Exception Type: {type(err)}")
            return False
        return True

    def save_screen_shot(self, elem, file_name):
        """ It's a quick solution to scroll to element to take a screenshot"""
        # Scroll down to take a screenshot
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'end', inline: 'nearest'});", elem)
        self.driver.get_screenshot_as_file(file_name)
