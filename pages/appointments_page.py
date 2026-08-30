from datetime import datetime, timedelta

from playwright.sync_api import expect

from pages.base_page import BasePage


class AppointmentsPage(BasePage):

    def go_to_appointments(self):
        self.page.get_by_role(
            "link",
            name="Appointments",
            exact=True
        ).click()

    def verify_appointment_exists(self):
        expect(
            self.page.get_by_role(
                "button",
                name="Reschedule"
            ).first
        ).to_be_visible()

    def click_reschedule(self):
        # Keep a reference to the appointment card being modified.
        reschedule_button = self.page.get_by_role(
            "button",
            name="Reschedule"
        ).first

        self.appointment_card = reschedule_button.locator(
            "xpath=../../.."
        )

        expect(self.appointment_card).to_be_visible()

        # Store the original appointment date/time.
        original_date_time = (
            self.appointment_card
            .locator("p")
            .first
            .inner_text()
        )

        self.original_date, self.original_time = (
            original_date_time.split(" • ")
        )

        reschedule_button.click()

    def select_date(self):
        original_date = datetime.strptime(
            self.original_date,
            "%m/%d/%Y"
        ).date()

        new_date = original_date + timedelta(days=1)

        self.new_date = new_date.strftime("%Y-%m-%d")
        self.display_date = new_date.strftime("%-m/%-d/%Y")

        date_input = self.page.locator("input[type='date']")

        date_input.fill(self.new_date)

        time_select = self.page.locator("select").last

        # Wait until the application loads at least one
        # available time slot.
        expect(
            time_select.locator("option")
        ).not_to_have_count(1, timeout=5000)

    def select_time(self):
        time_select = self.page.locator("select").last

        options = time_select.locator("option").all()

        available_times = []

        for option in options:
            value = option.get_attribute("value")

            if value:
                available_times.append(value)

        if not available_times:
            raise AssertionError(
                "No available time slots were found"
            )

        different_times = [
            time
            for time in available_times
            if time != self.original_time
        ]

        if not different_times:
            raise AssertionError(
                f"No time slot differs from original time "
                f"{self.original_time}"
            )

        self.new_time = different_times[0]

        time_select.select_option(self.new_time)


    def click_confirm(self):
        self.page.get_by_role(
            "button",
            name="Confirm"
        ).click()

    def verify_success_message(self):
        expect(
            self.page.get_by_text(
                "Appointment rescheduled successfully",
                exact=True
            )
        ).to_be_visible()

    def verify_new_date_and_time(self):
        appointment_text = (
            f"{self.display_date} • {self.new_time}"
        )

        # Validate the new date/time inside the SAME appointment card
        # that was modified.
        expect(
            self.appointment_card.get_by_text(
                appointment_text,
                exact=True
            )
        ).to_be_visible()