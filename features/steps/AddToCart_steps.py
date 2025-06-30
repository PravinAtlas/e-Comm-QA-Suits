from behave import given, when, then
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage



@when('the userr logs in with username {username} and password {password}')
def login_with_credentials_typo(context, username, password):
    login_page = LoginPage(context.page)
    login_page.login(username, password)


@when('the user adds the product "{product_name}" to the cart')
def add_product_to_cart(context, product_name):
    product_page = ProductsPage(context.page)
    product_page.add_product_to_cart(product_name)

@when('the user navigates to the cart page')
def navigate_to_cart_page(context):
    context.cart_page = CartPage(context.page)
    context.cart_page.goto()

@then('the cart should contain the product "{product_name}"')
def verify_product_in_cart(context, product_name):
    assert context.cart_page.is_product_in_cart(product_name), f"Product '{product_name}' not found in cart."




