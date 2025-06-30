from behave import when, then
from pages.products_page import ProductsPage
from utils.image_comparator import ImageComparator
import os

@when('the user captures the image of {product_name}')
def capture_product_image_for_comparison(context, product_name):
    context.products_page = ProductsPage(context.page)
    # Click on the product first
    context.products_page.click_on_product(product_name)
    # Save the screenshot after navigating to the product detail page
    context.captured_image_path = f"tests/temp/{product_name}.png"
    context.products_page.capture_product_image(product_name, context.captured_image_path)

@then('the product image should match the baseline for {product_name}')
def verify_product_image_matches_baseline(context, product_name):
    baseline_path = f"tests/baseline_images/{product_name}.png"
    assert os.path.exists(baseline_path), f"Baseline image not found: {baseline_path}"
    assert ImageComparator.compare_images(context.captured_image_path, baseline_path), \
        f"Product image for '{product_name}' does not match the baseline."