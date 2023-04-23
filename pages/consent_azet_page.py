from pages.base_page import BasePage


class ConsentPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        page.wait_for_load_state("networkidle")
        self.consent_title_locator = page.frame_locator("iframe[title=\"SP Consent Message\"]")
        self.consent_accept_all_locator = self.consent_title_locator.get_by_role("button", name="Prijať všetko")

    def assert_correctly_loaded(self):
        pass

    def accept_consent(self):
        if self.consent_accept_all_locator.is_visible():
            self.consent_accept_all_locator.click()
