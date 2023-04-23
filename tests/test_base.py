from playwright.sync_api import Page

from pages.consent_azet_page import ConsentPage
from pages.login_azet_page import LoginAzetPage

BASE_PAGE = "https://mail.azet.sk"


def login_to_azet_email(page: Page, username, password):
    page.goto(BASE_PAGE)
    consent_page = ConsentPage(page)
    consent_page.accept_consent()
    login_page = LoginAzetPage(page)
    login_page.fill_username(username)
    login_page.fill_password(password)
    login_page.confirm_login()
    return login_page
