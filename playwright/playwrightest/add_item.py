import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.parametrize("run_id", [1, 2, 3])
def test_login(run_id):
    print(f"\n🧪 Running test {run_id}...")

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
            print(f"✅ Test {run_id} passed: Successfully logged in.")
        except AssertionError:
            screenshot_path = f"screenshots/test_login_failed_{run_id}.png"
            page.screenshot(path=screenshot_path)
            print(f" Test {run_id} failed: Screenshot saved to {screenshot_path}")
            raise

        browser.close()