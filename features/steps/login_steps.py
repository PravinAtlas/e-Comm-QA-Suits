# steps for login.feature
from behave import given, when, then
from pages.login_page import LoginPage


@given("the user is on the login page")
def ensure_user_is_on_login_page(context):
    context.login_page = LoginPage(context.page)
    context.login_page.verify_login_page()


@when("the user logs in with {username} and {password}")
def login_with_credentials(context, username, password):
    context.login_result = context.login_page.login_and_validate(username, password)


@then("the login attempt should behave as expected for user {username}")
def verify_login_behavior_for_user(context, username):
    expected_results = {
        "standard_user": "success",
        "locked_out_user": "Epic sadface: Sorry, this user has been locked out.",
        "problem_user": "success",
        "performance_glitch_user": "success",
        "error_user": "Epic sadface: Username and password do not match any user in this service",
        "visual_user": "success",
    }
    expected = expected_results.get(username, None)
    assert expected is not None, f"No expected result defined for user {username}"
    assert context.login_result == expected or (
        expected == "success" and context.login_result == "success"
    ), f"User: {username} - Expected: {expected}, Got: {context.login_result}"
