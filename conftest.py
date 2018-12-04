import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
from selenium.common.exceptions import WebDriverException


@pytest.fixture(scope="function")
def driver_init(request):
    try:
        web_driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
        web_driver.get('http://google.ru')
    except WebDriverException:
        sleep(60)
        web_driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
        web_driver.get('http://google.ru')
    web_driver.set_window_size(1920, 1080)
    web_driver.implicitly_wait(30)
    request.cls.driver = web_driver
    yield
    web_driver.quit()
