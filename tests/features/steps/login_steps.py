from behave import given, when, then

from pages.login_page import LoginPage


@given("The patient is at the login page")
def step_patient_at_login_page(context):
    context.login_page = LoginPage(context.page)


@when("The patient fills in his email and password")
def step_patient_fills_credentials(context):
    context.login_page.fill_credentials(
        context.email,
        context.password
    )


@when("The patient clicks on the Sign In button")
def step_click_sign_in(context):
    context.login_page.click_sign_in()


@then("The patient can see the dashboard page")
def step_dashboard_visible(context):
    context.login_page.verify_dashboard()
    