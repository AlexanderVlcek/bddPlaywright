from abc import abstractmethod

from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.assert_correctly_loaded()

    @abstractmethod
    def assert_correctly_loaded(self):
        pass
