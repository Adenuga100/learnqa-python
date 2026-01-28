# pages/search_page.py
from playwright.sync_api import Page

class SearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.get_by_placeholder("Search docs")

    def navigate(self):
        self.page.goto("https://playwright.dev/python/")

    def search_for(self, text: str):
        self.search_input.fill(text)
        self.page.keyboard.press("Enter")