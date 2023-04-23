from playwright.sync_api import expect

from pages.base_page import BasePage


class NewAzetMailPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.contacts = page.get_by_role("link", name="#", exact=True)
        self.receiver_input = page.locator("css=input#od")
        self.subject = page.get_by_label("Predmet")
        self.body = page.frame_locator("iframe[class=\"cke_wysiwyg_frame cke_reset\"]").locator("body")
        self.send_email_button = page.get_by_role("button", name="Odoslať")

    def assert_correctly_loaded(self):
        expect(self.contacts).to_be_visible()
        expect(self.receiver_input).to_be_visible()
        expect(self.subject).to_be_visible()
        expect(self.body).to_be_visible()

    def select_alexander_vlcek_email(self):
        self.contacts.click()
        self.page.locator("#kontaktyPreOdoslanieTo").get_by_text("Alexander Vlček").click()
        assert self.receiver_input.get_attribute("value").__contains__("alesvlcek")

    def fill_subject(self, some_subject):
        self.subject.click()
        self.subject.fill(some_subject)

    def fill_message_body(self, message):
        self.body.click()
        self.body.fill(message)

    def send_email(self):
        self.send_email_button.first.click()
