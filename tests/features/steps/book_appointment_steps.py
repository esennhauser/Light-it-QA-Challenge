from behave import given, when, then

from pages.book_appointment_page import BookAppointmentPage


@when('The patient clicks on the Book Appointment button')
def step_click_book_appointment(context):
    context.book_appointment_page = BookAppointmentPage(context.page)
    context.book_appointment_page.click_book_appointment()


@then("The book appointment form is displayed")
def step_book_appointment_form_displayed(context):
    context.book_appointment_page.verify_form_is_displayed()


@then("The doctor field is visible")
def step_doctor_field_visible(context):
    context.book_appointment_page.verify_doctor_field_is_visible()


@then("The date field is visible")
def step_date_field_visible(context):
    context.book_appointment_page.verify_date_field_is_visible()


@then("The time slot field is visible")
def step_time_slot_field_visible(context):
    context.book_appointment_page.verify_time_field_is_visible()


@then("The notes field is visible")
def step_notes_field_visible(context):
    context.book_appointment_page.verify_notes_field_is_visible()


@then("The Book Appointment button is visible")
def step_book_button_visible(context):
    context.book_appointment_page.verify_book_button_is_visible()
    