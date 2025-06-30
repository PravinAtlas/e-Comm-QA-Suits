class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("id=user-name")
        self.password_input = page.locator("id=password")
        self.login_button = page.locator("id=login-button")
        self.error_message = page.locator('[data-test="error"]')

    def goto(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def is_logged_in(self):
        return self.page.url == "https://www.saucedemo.com/inventory.html"

    def get_error_message(self):
        if self.error_message.is_visible():
            return self.error_message.inner_text()
        return None

    def login_and_validate(self, username, password):
        self.login(username, password)
        if self.is_logged_in():
            return "success"
        else:
            return self.get_error_message() or "unknown error"

    def verify_login_page(self):
        """Check if the login button is present. If not, redirect to the login page URL."""
        try:
            if not self.page.locator(
                'input[type="submit"], [data-test="login-button"]'
            ).is_visible():
                self.goto()
        except Exception:
            self.goto()
