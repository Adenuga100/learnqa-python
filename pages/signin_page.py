# pages/search_page.py
import time
from itertools import count

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
        self._items = page.get_by_role("heading", name="Drag and Drop Practice")
        self._views_delayed_elements = page.get_by_text('✓ Element appeared after 5 second delay!')
        self._views_last_item = page.get_by_text('Dynamic Item 5')

    def navigate(self):
        self.page.goto("https://www.learnaqa.info/")

    def fill_email(self):
        random_id = str(uuid.uuid4())[:3]
        random_email = f"user_{random_id}@testmail.com"
        self._email.fill(random_email)
        return

    def email_input(self, email):

        self._email.fill(email)

    def slide_menu(self, menu):
        # _menu = self.page.get_by_role("link", name="{menu}")
        _menu = self.page.locator(f"//nav[@class='p-4 space-y-1']//span[text()='{menu}']")
        _menu.click()

    def button_as(self, btn):
        # _menu = self.page.get_by_role("link", name="{menu}")
        _button_as = self.page.get_by_role("button", name=f'{btn}')
        _button_as.click()
        time.sleep(6)


    def start_practice_button(self, name):
        _practice = self.page.locator(f"//div[contains(@class,'card')][.//span[normalize-space()='{name}']]//button")
        _practice.click()

    def drag_and_drop_items(self):
        _drag= self.page.locator("//div[@class='space-y-3 min-h-[200px]']//div[contains(@id,'item')]")
        _drop = self.page.locator("//div[contains(@id,'drop-zone')]")
        # count= _drag.count()

        # for i in range(count):
        #     time.sleep(2)
        #     _drag.nth(0).drag_to(_drop)

        while _drag.count()>0:
            # context.page.pause()
            _drag.nth(0).drag_to(_drop)

    def scroll_to_dynamic_items(self):
        _scroll_to_dynamic_items= self.page.locator("[class='jsx-5befb7a8f6657e3c space-y-2 max-h-60 overflow-y-auto'] [class*='ajax-item']")

        # count= _drag.count()

        # for i in range(count):
        #     time.sleep(2)
        #     _drag.nth(0).drag_to(_drop)
        last_count = 0

        while True:
            count = _scroll_to_dynamic_items.count()

            if count == last_count:
                break  # no new items loaded

            last_count = count
            _scroll_to_dynamic_items.nth(count - 1).scroll_into_view_if_needed()

        # while _scroll_to_dynamic_items.count()>0:
        #     _scroll_to_dynamic_items.scroll_into_view_if_needed()




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

    def views_item(self):
         return self._items.text_content()

    def views_delayed_elements(self):
         return self._views_delayed_elements.text_content()

    def views_last_item(self):
         return self._views_last_item.text_content()



    # def get_error_message(self):
    #     return self._error_msg.text_content()