from behave import given, when, then

from pages.login_page import LoginPage
from pages.appointments_page import AppointmentsPage


@given("A patient is logged on the Medical Appointment platform")
def step_patient_is_logged_in(context):
    context.login_page = LoginPage(context.page)

    context.login_page.fill_credentials(
        context.email,
        context.password
    )

    context.login_page.click_sign_in()
    context.login_page.verify_dashboard()


@given("The patient is on the appointments page")
def step_patient_on_appointments_page(context):
    context.appointments_page = AppointmentsPage(context.page)
    context.appointments_page.go_to_appointments()


@given("The patient has at least one appointment")
def step_patient_has_appointment(context):
    context.appointments_page.verify_appointment_exists()


@when("The patient clicks on the Reschedule button")
def step_click_reschedule(context):
    context.appointments_page.click_reschedule()


@when("The patient selects a date and a time")
def step_select_date_and_time(context):
    context.appointments_page.select_date()
    context.appointments_page.select_time()


@when("The patient clicks on the Confirm button")
def step_click_confirm(context):
    context.appointments_page.click_confirm()


@then("The UI shows a success message")
def step_success_message(context):
    context.appointments_page.verify_success_message()


@then("The appointment shows the new date and time selected")
def step_new_date_and_time(context):
    context.appointments_page.verify_new_date_and_time()
    