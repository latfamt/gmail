import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
from urllib3.exceptions import ProtocolError


@pytest.fixture(scope="function")
def driver_init(request):
    try:
        web_driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
        web_driver.get('http://google.ru')
    except ProtocolError:
        sleep(30)
        web_driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
        web_driver.get('http://google.ru')
    web_driver.set_window_size(1920, 1080)
    web_driver.implicitly_wait(30)
    request.cls.driver = web_driver
    yield
    web_driver.quit()


def pytest_addoption(parser):
    parser.addoption("--sender_email", action="store")
    parser.addoption("--sender_password", action="store")

    parser.addoption("--receiver_email", action="store")
    parser.addoption("--receiver_password", action="store")


def pytest_generate_tests(metafunc):
    option_sender_email = metafunc.config.option.sender_email
    option_sender_password = metafunc.config.option.sender_password
    option_receiver_email = metafunc.config.option.receiver_email
    option_receiver_password = metafunc.config.option.receiver_password

    if "sender_email" in metafunc.fixturenames and option_sender_email is not None:
        metafunc.parametrize("sender_email", [option_sender_email])
    if "sender_password" in metafunc.fixturenames and option_sender_password is not None:
        metafunc.parametrize("sender_password", [option_sender_password])
    if "receiver_email" in metafunc.fixturenames and option_receiver_email is not None:
        metafunc.parametrize("receiver_email", [option_receiver_email])
    if "receiver_password" in metafunc.fixturenames and option_receiver_password is not None:
        metafunc.parametrize("receiver_password", [option_receiver_password])