from behave import when, then
from utils.api_helpers import APIHelper
from utils.logger import Logger

logger = Logger()


def expect(condition, message):
    if not condition:
        raise AssertionError(message)


@when("the client requests the list of users on page {page:d}")
def request_list_of_users(context, page):
    context.api_response = APIHelper.get("/users", params={"page": page})
    print(context.api_response)
    logger.info(f"GET /users?page={page} - Status: {context.api_response.status_code}")
    logger.info(f"Response Body: {context.api_response.text}")


@then("the response status code should be {status_code:d}")
def check_status_code(context, status_code):
    logger.info(
        f"Asserting status code: Expected {status_code}, Got {context.api_response.status_code}"
    )
    expect(
        context.api_response.status_code == status_code,
        f"Expected status code {status_code}, got {context.api_response.status_code}",
    )


@then("the response should contain a user with email {email}")
def response_should_contain_email(context, email):
    data = context.api_response.json().get("data", [])
    emails = [user["email"] for user in data]
    logger.info(f"Checking if email '{email}' is in response emails: {emails}")
    expect(email in emails, f"Email {email} not found in response")
