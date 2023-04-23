from playwright.sync_api import expect

from pages.base_page import BasePage
from util.util_playwright import WaitUntil


class LeftBoxAzetMailPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.new = page.get_by_role("link", name="n Písať nový mail")
        self.inbox = page.get_by_role("link", name="Doručené")
        self.draft = page.get_by_role("link", name="Rozpísané")
        self.planed = page.get_by_role("link", name="Naplánované")
        self.unread = page.get_by_role("link", name="Neprečítané")
        self.sent = page.locator("#js_idfolderListItem_sent__")
        self.sent_count = self.sent.locator(".count")

    def assert_correctly_loaded(self):
        expect(self.new).to_be_visible()
        expect(self.sent).to_be_visible()

    def start_new_email(self):
        self.new.click()

    def wait_for_email_is_sent(self, sent_emails):
        i = 0
        max_count_iteration = 30
        while i < max_count_iteration:
            self.page.wait_for_timeout(1000)
            self.page.reload(wait_until=WaitUntil.DOM_CONTENT_LOADED.value)
            count = self.count_of_sent_emails()
            if sent_emails + 1 == count:
                break
            i += 1
        if i == max_count_iteration:
            raise AssertionError("Email was sent but not verified in azet page")

    def count_of_sent_emails(self):
        return int(self.sent_count.text_content())
