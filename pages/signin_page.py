# pages/search_page.py
from playwright.sync_api import Page
# pages/signin_page.py
from playwright.sync_api import Page

class SigninPage:
    def __init__(self, page: Page):
        self.page = page
        self._signin_btn = page.get_by_role('button', name='Sign In')
        self._email = page.locator('[name="email"]')
        self._password = page.locator('[name="password"]')
        self._signin_button = page.get_by_role('button', name='Sign In')
        self._error_msg = page.locator("[data-test='error']")
        self._inventory = page.get_by_text("Practice Dashboard")

    def navigate(self):
        self.page.goto("https://www.learnaqa.info/")

    def fill_email(self, username):
        self._email.fill(username)

    def signin_button(self):
        self._signin_btn.nth(1).click()


    def fill_password(self, password):
        self._password.fill(password)

    def login_button(self):
        self._signin_button.click()

    def inventory_button(self):
         return self._inventory.text_content()


    # def get_error_message(self):
    #     return self._error_msg.text_content()