from ..pages.elements import ElementsPage

import logging
LOGGER = logging.getLogger()

url = 'https://demoqa.com'


def test_welcome_text(driver):
    LOGGER.info('test_welcome_text')
    page = ElementsPage(driver)
    LOGGER.info('test_welcome_text2')
    page.open(url)
    LOGGER.info('test_welcome_text3')
    page.go_to_elements_page()
    LOGGER.info('test_welcome_text4')
    page.check()

