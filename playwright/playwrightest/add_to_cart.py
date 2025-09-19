import pytest
import random
from playwright.sync_api import sync_playwright

@pytest.mark.parametrize("run_id", [1, 2, 3])
def test_login_and_add_item(run_id):
    print(f"\n Running test {run_id}...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")

        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.press("#password", "Enter")
        page.wait_for_load_state("networkidle")

        try:
            assert "inventory.html" in page.url
            print(f" Test {run_id} passed: Successfully logged in.")

            add_buttons = page.query_selector_all("button.btn_inventory")
           
            if not add_buttons:
                raise Exception("No items found to add to cart.")
            random_item = random.choice(add_buttons)
            item_name = random_item.evaluate("el => el.closest('.inventory_item').querySelector('.inventory_item_name').textContent")
            random_item.click()
            print(f" Added item to cart: {item_name}")

           
            page.click(".shopping_cart_link")
            page.wait_for_load_state("networkidle")

            cart_items = page.locator(".cart_item .inventory_item_name").all_text_contents()
            assert item_name in cart_items
            print(f" Verified item in cart: {item_name}")

        except Exception as e:
            screenshot_path = f"screenshots/test_failed_{run_id}.png"
            page.screenshot(path=screenshot_path)
            print(f" Test {run_id} failed: {e}\n Screenshot saved to {screenshot_path}")
            raise

        browser.close()