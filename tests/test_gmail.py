import pytest
from data import test_message_text, test_message_subject, reply_message_text
from pages.google_page import go_to_mail
from pages.inbox_page import add_mail, enter_receiver_email, enter_subject, enter_message, send_message, open_message, \
    logout, change_account, text_of_message, reply, check_message_as_read, notification
from pages.logon_page import enter_email, enter_password


@pytest.mark.usefixtures("driver_init")
@pytest.mark.unit
class TestGmail:
    def test_gmail(self, sender_email, sender_password, receiver_email, receiver_password):
        go_to_mail(self.driver)
        enter_email(self.driver, email=sender_email)
        enter_password(self.driver, password=sender_password)
        add_mail(self.driver)
        enter_receiver_email(self.driver, email=receiver_email)
        enter_subject(self.driver, subject=test_message_subject)
        enter_message(self.driver, message_text=test_message_text)
        send_message(self.driver)
        assert notification(self.driver)
        logout(self.driver)
        change_account(self.driver)
        enter_email(self.driver, email=receiver_email)
        enter_password(self.driver, password=receiver_password)
        check_message_as_read(self.driver, message_subject=test_message_subject)
        assert notification(self.driver)
        open_message(self.driver, message_subject=test_message_subject)
        assert text_of_message(self.driver) == test_message_text
        reply(self.driver)
        enter_message(self.driver, message_text=reply_message_text)
        send_message(self.driver)
        assert notification(self.driver)
