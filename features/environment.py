from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright

def before_all(context):
    print("[BEFORE ALL] Test suite setup.")

    context.playwright = sync_playwright().start()

        # Optionally, navigate to the base URL if needed

def after_all(context):
    print("[AFTER ALL] Test suite teardown.")
    if hasattr(context, "page"):
        context.page.close()
    if hasattr(context, "browser"):
        context.browser.close()
    if hasattr(context, "playwright"):
        context.playwright.stop()

def before_scenario(context, scenario):

    print(f"[BEFORE SCENARIO] Starting scenario: {scenario.name}")
    # Reset state or navigate to login page if needed
    if 'api' in scenario.effective_tags:

        return
    context.browser = context.playwright.chromium.launch(headless=False, channel="chrome", args=["--start-maximized"])
    context.page = context.browser.new_page()
    context.page.goto("https://www.saucedemo.com/")

def after_scenario(context, scenario):
    print(f"[AFTER SCENARIO] Finished scenario: {scenario.name}")
    # Optionally, clear cookies or local storage
    if hasattr(context, "page"):
        context.page.context.clear_cookies()
        context.page.goto("https://www.saucedemo.com/")
