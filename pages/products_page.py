class ProductsPage:
    def __init__(self, page):
        self.page = page

    def add_product_to_cart(self, product_name):
        # Locate the product card by name and click its corresponding 'Add to cart' button
        product_locator = self.page.locator(
            f".inventory_item:has-text('{product_name}')"
        )
        add_button = product_locator.locator("button:has-text('Add to cart')")
        add_button.click()

    def capture_product_image(self, product_name, save_path):
        # On the detail page, the image has class 'inventory_details_img'
        image_locator = self.page.locator(".inventory_details_img")
        image_locator.wait_for(state="visible", timeout=5000)
        image_locator.first.screenshot(path=save_path)

    def click_on_product(self, product_name):
        # Use a dynamic XPath to find the product link by its visible text
        # xpath = f"//div[contains(@class, 'inventory_item')]//a[contains(@class, 'inventory_item_name') and normalize-space(text())='{product_name}']"
        xpath = "//div[@class='inventory_item']/div[2]//a"
        product_link = self.page.locator(f"xpath={xpath}")
        print(
            "Product link count:", product_link.count()
        )  # Should be >= 1 if the product exists
        if product_link.count() > 0:
            print("Product link text:", product_link.first.text_content())
            product_link.first.wait_for(state="visible", timeout=5000)
            product_link.first.click()
        else:
            print("No product link found for:", product_name)
            raise Exception(f"Product '{product_name}' not found on inventory page.")
