from behave import given, when, then
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@when('the userrr logs in with {username} and {password}')
def login_with_credentials_typo(context, username, password):

    login_page = LoginPage(context.page)
    login_page.login(username, password)


@when('the user adds the following products to the cart')
def add_multiple_products_to_shopping_cart(context):
    product_page = ProductsPage(context.page)
    for row in context.table:
        product_name = row['products']

        product_page.add_product_to_cart(product_name)


@then('the cart should contain the following products')
def verify_products_present_in_shopping_cart(context):
    cart_page = CartPage(context.page)
    for row in context.table:
        product_name = row['products']
        assert cart_page.is_product_in_cart(product_name), f"Product '{product_name}' not found in cart."
