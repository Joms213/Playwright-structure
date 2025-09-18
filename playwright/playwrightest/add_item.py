import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.repeat(3)  
def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")

       
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")

        page.press("#password", "Enter")

        page.wait_for_load_state("networkidle")

        assert "inventory.html" in page.url

        browser.close()