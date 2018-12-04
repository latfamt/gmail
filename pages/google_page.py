from selenium.webdriver.common.by import By
from data import about_gmail_link

MAIL_LINK = By.CSS_SELECTOR, "a.gb_P[data-pid='23']"
ENTER_MAIL = By.CSS_SELECTOR, '.gmail-nav__nav-link__sign-in'


def go_to_mail(driver):
    driver.find_element(*MAIL_LINK).click()
    if about_gmail_link in driver.current_url:
        driver.find_element(*ENTER_MAIL).click()
