from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ADD_MAIL_BTN = By.CSS_SELECTOR, ".aic div[role=button]"
SENDER_EMAIL_FIELD = By.CSS_SELECTOR, "textarea[name=to]"
SUBJECT_FIELD = By.CSS_SELECTOR, "input[name=subjectbox]"
MESSAGE_FIELD = By.CSS_SELECTOR, ".Am.Al.editable"
SEND_BUTTON = By.CSS_SELECTOR, ".aoO"
NOTIFICATION = By.CSS_SELECTOR, ".aT"
READ_BTN = By.CSS_SELECTOR, "div[gh='mtb'] .bzn .G-tF div:nth-of-type(3) div.m9"

ACCOUNT_MENU_BTN = By.CSS_SELECTOR, ".gb_ab"
LOGOUT_BTN = By.CSS_SELECTOR, "#gb_71"

ACTIVE_ACCOUNT_BTN = By.CSS_SELECTOR, "#profileIdentifier"
CHANGE_ACC_BTN = By.CSS_SELECTOR, "#identifierLink"

MESSAGE_TEXT = By.CSS_SELECTOR, ".ii.gt [dir='ltr']"
REPLY_BTN = By.CSS_SELECTOR, ".ams.bkH"


def add_mail(driver):
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable(ADD_MAIL_BTN)).click()


def enter_receiver_email(driver, email):
    driver.find_element(*SENDER_EMAIL_FIELD).send_keys(email)


def enter_subject(driver, subject):
    driver.find_element(*SUBJECT_FIELD).send_keys(subject)


def enter_message(driver, message_text):
    driver.find_element(*MESSAGE_FIELD).send_keys(message_text)


def send_message(driver):
    driver.find_element(*SEND_BUTTON).click()


def open_message(driver, message_subject):
    MESSAGE = By.XPATH, f"//span[contains(text(), '{message_subject}')]//ancestor::td[@class='xY a4W']"
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(MESSAGE)).click()


def logout(driver):
    driver.find_element(*ACCOUNT_MENU_BTN).click()
    driver.find_element(*LOGOUT_BTN).click()


def change_account(driver):
    driver.find_element(*ACTIVE_ACCOUNT_BTN).click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable(CHANGE_ACC_BTN)).click()


def text_of_message(driver):
    return WebDriverWait(driver, 60).until(EC.visibility_of_element_located(MESSAGE_TEXT)).text


def reply(driver):
    driver.find_element(*REPLY_BTN).click()


def check_message_as_read(driver, message_subject):
    CHECKBOX = By.XPATH, f"//span[contains(text(), '{message_subject}')]/ancestor::div[@role='main']//td[contains(@class, 'oZ-x3')]"
    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located(CHECKBOX)).click()
    except TimeoutException:
        driver.refresh()
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located(CHECKBOX)).click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable(READ_BTN)).click()


def notification(driver):
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(NOTIFICATION))
    WebDriverWait(driver, 60).until(EC.staleness_of(driver.find_element(*NOTIFICATION)))
    return True
