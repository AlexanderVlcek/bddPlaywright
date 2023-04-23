from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginAzetPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        page.wait_for_load_state("networkidle")
        self.user_name_input_field_locator = page.get_by_placeholder("Zadaj názov účtu")
        self.password_input_field_locator = page.get_by_placeholder("Zadaj svoje heslo")
        self.login_button_locator = page.get_by_role("button", name="Prihlásiť sa")

    def assert_correctly_loaded(self):
        expect(self.user_name_input_field_locator).to_be_visible()
        expect(self.password_input_field_locator).to_be_visible()
        expect(self.login_button_locator).to_be_visible()

    def fill_username(self, username):
        self.user_name_input_field_locator.click()
        self.user_name_input_field_locator.fill(username)

    def fill_password(self, password):
        self.password_input_field_locator.click()
        self.password_input_field_locator.fill(password)

    def confirm_login(self):
        self.login_button_locator.click()
