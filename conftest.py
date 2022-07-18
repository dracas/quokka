import pytest
import os
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options as ChromeOptions

import logging
LOGGER = logging.getLogger()


@pytest.fixture
def driver(request):
    load_dotenv()
    options = ChromeOptions()
    options.browser_version = 'latest'
    options.platform_name = 'Windows 10'

    LOGGER.debug(os.environ["SAUCE_USERNAME"])
    LOGGER.debug(os.environ["SAUCE_ACCESS_KEY"])

    sauce_options = {'username': os.environ["SAUCE_USERNAME"],
                     'accessKey': os.environ["SAUCE_ACCESS_KEY"],
                     'name': request.node.name}

    options.set_capability('sauce: options', sauce_options)
    sauce_url = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"

    driver = webdriver.Remote(command_executor=sauce_url, options=options)

    yield driver
    if driver is not None:
        sauce_result = "failed" if request.session.testsfailed == 1 else "passed"
        driver.execute_script("sauce:job-result={}".format(sauce_result))

        driver.quit()
