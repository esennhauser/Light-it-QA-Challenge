from playwright.sync_api import expect

from pages.base_page import BasePage

class BookAppointmentPage(BasePage):


    def click_book_appointment(self):
        self.page.locator(
            'a[href="/appointments/new"]'
        ).click()

    def verify_form_is_displayed(self):
        expect(
            self.page.get_by_role(
                "heading",
                name="Book Appointment",
                exact=True
            )
        ).to_be_visible()

    def verify_doctor_field_is_visible(self):
        expect(
            self.page.locator("#doctor_id")
        ).to_be_visible()

    def verify_date_field_is_visible(self):
        expect(
            self.page.locator("#appointment_date")
        ).to_be_visible()

    def verify_time_field_is_visible(self):
        expect(
            self.page.locator("#time_slot")
        ).to_be_visible()

    def verify_notes_field_is_visible(self):
        expect(
            self.page.locator("#notes")
        ).to_be_visible()

    def verify_book_button_is_visible(self):
        expect(
            self.page.get_by_test_id("submit-appointment")
        ).to_be_visible()
