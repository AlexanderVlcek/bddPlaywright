from pytest_bdd import scenario, given, when, then, parsers

from pages.azetMailPages.left_box_azet_mail_page import LeftBoxAzetMailPage
from pages.azetMailPages.new_azet_mail_page import NewAzetMailPage
from tests.test_base import login_to_azet_email


@scenario('../features/send_email_azet.feature', 'Send email')
def test_publish():
    pass


@given(parsers.parse('user with credentials "{username}", "{password}" is logged in azet email'))
def user_is_logged_in_azet_email(page, username, password):
    login_to_azet_email(page, username, password)


@when("starts to write new email")
def user_starts_to_write_new_email(page):
    left_box_azet_mail_page = LeftBoxAzetMailPage(page)
    left_box_azet_mail_page.start_new_email()


@when("chose email address from contacts")
def user_chose_email_from_contact_addresses(page):
    new_azet_mail_page = NewAzetMailPage(page)
    new_azet_mail_page.select_alexander_vlcek_email()


@when(parsers.parse('write message with text "{phrase}"'))
def write_message_with_text(page, phrase):
    new_azet_mail_page = NewAzetMailPage(page)
    new_azet_mail_page.fill_subject("Test email")
    new_azet_mail_page.fill_message_body(phrase)


@when("click send email", target_fixture='azet_fixture')
def click_send_email(page):
    left_box_azet_mail_page = LeftBoxAzetMailPage(page)
    count = left_box_azet_mail_page.count_of_sent_emails()
    new_azet_mail_page = NewAzetMailPage(page)
    new_azet_mail_page.send_email()
    return count


@then("email is sent")
def email_is_sent(page, azet_fixture):
    left_box_azet_mail_page = LeftBoxAzetMailPage(page)
    left_box_azet_mail_page.wait_for_email_is_sent(azet_fixture)
