from .base import BasePage
from selenium.webdriver.common.by import By

import logging
LOGGER = logging.getLogger()


class ElementsPage(BasePage):
    LOGGER.info('ElementsPage')

    def go_to_elements_page(self):
        LOGGER.info('go_to_elements_page')
        link = self.driver.find_element(By.CSS_SELECTOR, '.category-cards:first-child .card-body :first-child')
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", link)
        link.click()

    def check(self):
        LOGGER.info('check')
        text = self.driver.find_element(By.CSS_SELECTOR, ".col-md-6").text
        LOGGER.info('assert')
        assert text == 'Please select an item from left to start practice.'
