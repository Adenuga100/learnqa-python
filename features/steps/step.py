from behave import given, when, then, runner, When
# The import error usually disappears once __init__.py is added to the pages folder
from pages.signin_page import SigninPage

# @given('the user is on the login page')
# def go_to_login(context):
#     # We initialize it here, or better yet, in environment.py
#     context.login_page = LoginPage(context.page)
#     context.login_page.navigate()
#
# @when('the user enters "{username}" and "{password}"')
# def enter_credentials(context, username, password):
#     # Use context.login_page instead of passing it as an argument
#     context.login_page.login(username, password)
#
# @then('the user should be redirected to the inventory page')
# def verify_redirect(page):
#     assert "inventory.html" in page.url


@given(u'User is on the login page')
def step_impl(context):
    context.signin_page = SigninPage(context.page)
    context.signin_page.navigate()


@when(u'User enters email')
def step_impl(context):
    context.signin_page.fill_email()

@when(u'user click on signin button')
def step_impl(context:runner.Context):
    context.signin_page.signin_button()


@when(u'User enters as "{password}"')
def step_impl(context, password):
    context.signin_page.fill_password(password)


@when(u'User click on login button')
def step_impl(context):
    context.signin_page.login_button()

@when(u'user click on sign up button')
def step_impl(context):
    context.signin_page.sign_up_button()

@when(u'user enters full name as"{fullname}"')
def step_impl(context, fullname):
    context.signin_page.full_name(fullname)

@when(u'User click on create account button')
def step_impl(context):
    context.signin_page.create_account_button()

@then(u'User should be redirected to the inventory page')
def step_impl(context):
    context.signin_page.inventory_button()
    # assert "inventory.html" in  context.page.url
    # raise StepNotImplementedError(u'Then user click on login button')


@when("User click on cookies")
def step_impl(context:runner.Context):
    context.signin_page.cookies_button()


@When('User enters "{email}"')
def step_impl(context:runner.Context, email):
    context.signin_page.email_input(email)

@When('User click on start practice as"{name}"')
def step_impl(context: runner.Context, name):
    # context.page.pause()
    context.signin_page.start_practice_button(name)


@When("user drag and drop all the items")
def step_impl(context:runner.Context):
    context.signin_page.drag_and_drop_items()


@then("user drop all the items successfully")
def step_impl(context:runner.Context):
    context.signin_page.views_item()


@when('User click "{menu}" on the slide menu')
def step_impl(context:runner.Context, menu):
    # context.page.pause()
    context.signin_page.slide_menu(menu)


@When('User click on button as"{btn}"')
def step_impl(context:runner.Context, btn):
    context.signin_page.button_as(btn)



@then("user views delayed elements successfully")
def step_impl(context:runner.Context):
   context.signin_page.views_delayed_elements()


@When("user scroll to each dynamic items")
def step_impl(context:runner.Context):
    context.signin_page.scroll_to_dynamic_items()


@then("user views last item")
def step_impl(context:runner.Context):
   context.signin_page.views_last_item()