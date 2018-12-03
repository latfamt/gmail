from selenium.webdriver.common.by import By
from data import about_gmail_link

MAIL_LINK = By.CSS_SELECTOR, ".gb_P[href='https://mail.google.com/mail/?tab=wm']"
ENTER_MAIL = By.CSS_SELECTOR, '.gmail-nav__nav-link__sign-in'


def go_to_mail(driver):
    driver.find_element(*MAIL_LINK).click()
    if driver.current_url == about_gmail_link:
        driver.find_element(*ENTER_MAIL).click()
