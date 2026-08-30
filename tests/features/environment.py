import os

import allure
from dotenv import load_dotenv

from driver.driver import start_browser


load_dotenv()


def before_scenario(context, scenario):
    context.email = os.getenv("MEDAPPOINT_EMAIL")
    context.password = os.getenv("MEDAPPOINT_PASSWORD")
    context.base_url = os.getenv(
        "MEDAPPOINT_URL",
        "https://light-it-qa-challenge.vercel.app"
    )

    if not context.email or not context.password:
        raise RuntimeError(
            "MEDAPPOINT_EMAIL and MEDAPPOINT_PASSWORD must be configured in .env file"
        )

    context.playwright, context.browser, context.page = start_browser()

    context.page.goto(f"{context.base_url}/login")


def after_step(context, step):
    if hasattr(context, "page"):
        screenshot = context.page.screenshot()
        allure.attach(
            screenshot, name=f"{step.name}",
            attachment_type=allure.attachment_type.PNG
            )


def after_scenario(context, scenario):
    context.browser.close()
    context.playwright.stop()