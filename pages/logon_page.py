from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import recovery_page_url

EMAIL_FIELD = By.CSS_SELECTOR, "#identifierId"
EMAIL_NEXT_BTN = By.CSS_SELECTOR, "#identifierNext"
PASSWORD_FIELD = By.CSS_SELECTOR, "input[name='password']"
PASSWORD_NEXT_BTN = By.CSS_SELECTOR, "#passwordNext"
READY_BTN = By.CSS_SELECTOR, ".yKBrKe [role=button]"


def enter_email(driver, email):
    driver.find_element(*EMAIL_FIELD).send_keys(email)
    driver.find_element(*EMAIL_NEXT_BTN).click()


def enter_password(driver, password):
    driver.find_element(*PASSWORD_FIELD).send_keys(password)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable(PASSWORD_NEXT_BTN)).click()
    if recovery_page_url in driver.current_url:
        driver.find_element(*READY_BTN).click()
