import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        yield browser
        browser.close()
@pytest.mark.repeat(3)  

@pytest.mark.parametrize("link_name, expected_url_part", [
    ("Docs", "/docs"),
    ("API", "/api"),
])
def test_navigation_links(browser, link_name, expected_url_part):
    page = browser.new_page()
    try:
        page.goto("https://playwright.dev/python")
        page.get_by_role('link', name=link_name).click()
        page.wait_for_load_state("load")
        assert expected_url_part in page.url
    except Exception as e:
        page.screenshot(path=f"{link_name}_error.png")
        raise e
    finally:
        page.close()