from abc import abstractmethod

from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    @abstractmethod
    def assert_correctly_loaded(self):
        pass
