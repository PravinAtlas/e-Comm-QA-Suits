class CartPage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto("https://www.saucedemo.com/cart.html")

    def is_product_in_cart(self, product_name):
        # Looks for the product name in the cart items
        return self.page.locator(f'.cart_item:has-text("{product_name}")').is_visible()
