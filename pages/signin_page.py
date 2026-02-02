# pages/search_page.py
from playwright.sync_api import Page
# pages/signin_page.py
import uuid
from playwright.sync_api import Page


class SigninPage:
    def __init__(self, page: Page):
        self.page = page
        self._signin_btn = page.get_by_role('button', name='Sign In')
        self._signup_button = page.get_by_role('button', name='Sign Up')
        self._email = page.locator('[name="email"]')
        self._name = page.locator('[name="full_name"]')
        self._password = page.locator('[name="password"]')
        self._signin_button = page.get_by_role('button', name='Sign In')
        self._create_button = page.locator('[type="submit"]')
        self._cookies_btn = page.get_by_role('button', name='Accept All')
        self._error_msg = page.locator("[data-test='error']")
        self._inventory = page.get_by_text("Practice Dashboard")

    def navigate(self):
        self.page.goto("https://www.learnaqa.info/")

    def fill_email(self):
        random_id = str(uuid.uuid4())[:3]
        random_email = f"user_{random_id}@testmail.com"
        self._email.fill(random_email)
        return

    def email_input(self, email):

        self._email.fill(email)

    def start_practice_button(self, name):
        self._email = self.page.locator(f"//div[contains(@class,'card')][.//span[normalize-space()='{name}']]//button")
        self._email.click()


    def signin_button(self):
        self._signin_btn.nth(1).click()


    def fill_password(self, password):
        self._password.fill(password)

    def login_button(self):
        self._signin_button.click()

    def sign_up_button(self):
        self._signup_button.nth(1).click()

    def full_name(self, fullname):
        self._name.fill(fullname)

    def create_account_button(self):
        self._create_button.click()

    def cookies_button(self):
        self._cookies_btn.click()

    def inventory_button(self):
         return self._inventory.text_content()


    # def get_error_message(self):
    #     return self._error_msg.text_content()