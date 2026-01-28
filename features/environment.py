from behave import runner
from playwright.sync_api import sync_playwright


def before_scenario(context, scenario):
    context.p = sync_playwright().start()
    context.browser = context.p.chromium.launch(headless=False)
    context.page = context.browser.new_page()

    def after_scenario(context, scenario):
        context.browser.close()
        # context.browser.quit()
        context.p.stop()