from behave import when, then
from utils.api_helpers import APIHelper
from utils.logger import Logger

logger = Logger()


@when("the client requests the list of users on page {page:d}")
def request_list_of_users(context, page):
    context.api_response = APIHelper.get_users(page)
    logger.info(f"GET /users?page={page} - Status: {context.api_response.status_code}")
    logger.info(f"Response Body: {context.api_response.text}")


@when("the client creates a user with name {name} and job {job}")
def create_user(context, name, job):
    payload = {"name": name, "job": job}
    logger.info(f"POST /users - Payload: {payload}")
    context.api_response = APIHelper.create_user(name, job)
    logger.info(f"Response Body: {context.api_response.text}")


@when("the client requests user with id {user_id:d}")
def request_single_user(context, user_id):
    context.api_response = APIHelper.get_user(user_id)
    logger.info(f"GET /users/{user_id} - Status: {context.api_response.status_code}")
    logger.info(f"Response Body: {context.api_response.text}")


@then("the response status code should be {status_code:d}")
def check_status_code(context, status_code):
    logger.info(
        f"Asserting status code: Expected {status_code}, Got {context.api_response.status_code}"
    )
    assert context.api_response.status_code == status_code


@then("the response should contain a user with email {email}")
def response_should_contain_email(context, email):
    data = context.api_response.json().get("data", [])
    emails = [user["email"] for user in data]
    logger.info(f"Checking if email '{email}' is in response emails: {emails}")
    assert email in emails, f"Email {email} not found in response"


@then("the response should contain the name {name}")
def response_should_contain_name(context, name):
    data = context.api_response.json()
    logger.info(f"Checking if name '{name}' is in response: {data}")
    assert data.get("name") == name, f"Name {name} not found in response"
