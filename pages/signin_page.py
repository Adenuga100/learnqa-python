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
        self._views_Last_Lazy_Loading_Items = page.locator('[class*="lazy-image-placeholder"]').last
        self._views_Infinite = page.get_by_text('No more items to load')
        self._views_hidden_element = page.get_by_text('Hidden element revealed!')
        self._generate_dynamic_content = page.locator('[id="dynamic-content"]')

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
        _button_as.scroll_into_view_if_needed()
        time.sleep(2)
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

    def scroll_to_lazy_loading_items(self):
        _scroll_To_Lazy_Loading_Items= self.page.locator("[class*='lazy-image-placeholder']")

        # count= _drag.count()

        # for i in range(count):
        #     time.sleep(2)
        #     _drag.nth(0).drag_to(_drop)
        last_count = 0

        while True:
            count = _scroll_To_Lazy_Loading_Items.count()

            if count == last_count:
                break  # no new items loaded

            last_count = count
            _scroll_To_Lazy_Loading_Items.nth(count-1).scroll_into_view_if_needed()

        # while _scroll_to_dynamic_items.count()>0:
        #     _scroll_to_dynamic_items.scroll_into_view_if_needed()

    def scroll_to_infinite_scroll(self):
        _scroll_To_Infinite_Scroll= self.page.locator("[class*='scroll-item p-3 bg-white rounded border']")
        last_count = 0
        while True:
            time.sleep(2)
            count = _scroll_To_Infinite_Scroll.count()

            if count == last_count:
                break  # no new items loaded

            last_count = count
            _scroll_To_Infinite_Scroll.nth(count-1).scroll_into_view_if_needed()
            time.sleep(6)
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

    def views_last_lazy_loading_items(self):
         return self._views_Last_Lazy_Loading_Items.text_content()

    def views_infinite_scroll(self):
         return self._views_Infinite.text_content()

    def views_hidden_element(self):
         return self._views_hidden_element.text_content()

    def generate_dynamic_content(self):
         return self._generate_dynamic_content.text_content()



    # def get_error_message(self):
    #     return self._error_msg.text_content()