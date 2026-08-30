import os

from playwright.sync_api import sync_playwright


def start_browser():
    playwright = sync_playwright().start()

    headless = os.getenv("HEADLESS", "false").lower() == "true"

    browser = playwright.chromium.launch(
        headless=headless
    )

    page = browser.new_page()

    return playwright, browser, page
