import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.repeat(5)  
def test_docs_navigation():
    print("🔧 Starting Playwright test...")

    with sync_playwright() as playwright:
        print(" Launching Chromium browser...")
        browser = playwright.chromium.launch(headless=False)

        page = browser.new_page()
        print(" Navigating to homepage...")
        page.goto("https://playwright.dev/python")

        print("🖱️ Clicking 'Docs' link...")
        docs_button = page.get_by_role('link', name="Docs")
        docs_button.click()

        page.wait_for_load_state("load")  # Wait for navigation to complete

        # ✅ Assertion: Check if URL contains '/docs'
        assert "/docs" in page.url, f"Expected '/docs' in URL, but got: {page.url}"
        print(" Navigation successful. Current URL:", page.url)

        print(" Closing browser...")
        browser.close()

    print(" Test completed.")