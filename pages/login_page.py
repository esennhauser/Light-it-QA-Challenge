from pages.base_page import BasePage
from playwright.sync_api import expect


class LoginPage(BasePage):

    EMAIL_INPUT = "#email"
    PASSWORD_INPUT = "#password"

    def fill_credentials(self, email, password):
        self.page.locator(self.EMAIL_INPUT).fill(email)
        self.page.locator(self.PASSWORD_INPUT).fill(password)

    def click_sign_in(self):
        self.page.get_by_role("button", name="Sign In").click()

    def verify_dashboard(self):
        dashboard_link = self.page.get_by_role(
            "link",
            name="Dashboard",
            exact=True
        )
        expect(dashboard_link).to_be_visible()