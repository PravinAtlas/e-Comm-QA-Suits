from playwright.sync_api import sync_playwright
from utils.logger import Logger

logger = Logger()


def before_all(context):

    logger.info("[BEFORE ALL] Test suite setup.".center(100))

    context.playwright = sync_playwright().start()

    # Optionally, navigate to the base URL if needed


def after_all(context):

    logger.info("[AFTER ALL] Test suite teardown.".center(100))
    if hasattr(context, "page"):
        context.page.close()
    if hasattr(context, "browser"):
        context.browser.close()
    if hasattr(context, "playwright"):
        context.playwright.stop()


def before_scenario(context, scenario):

    logger.info("[BEFORE SCENARIO] Starting scenario: {scenario.name}".center(100))
    # Reset state or navigate to login page if needed
    if "api" in scenario.effective_tags:
        return
    context.browser = context.playwright.chromium.launch(
        headless=False, channel="chrome", args=["--start-maximized"]
    )
    context.page = context.browser.new_page()
    context.page.goto("https://www.saucedemo.com/")


def after_scenario(context, scenario):
    logger.info(f"[AFTER SCENARIO] Finished scenario: {scenario.name}".center(100))
    if "api" not in scenario.effective_tags:
        # Optionally, clear cookies or local storage
        if hasattr(context, "page"):
            context.page.context.clear_cookies()
            context.page.goto("https://www.saucedemo.com/")
