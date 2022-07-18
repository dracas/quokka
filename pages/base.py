
import logging
LOGGER = logging.getLogger()


class BasePage:
    def __init__(self, driver):
        LOGGER.info('init')
        self.driver = driver

    def open(self, url):
        LOGGER.info('open')
        self.driver.get(url)
