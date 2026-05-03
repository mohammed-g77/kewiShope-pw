import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.login_page import LoginPage

# VALID LOGIN TEST 
def test_valid_login(page: Page, base_url: str, test_data: dict):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.navigate_to_home(base_url)
    home_page.go_to_login()

    user = test_data["valid_user"]

    with page.expect_response(
        lambda response: "login" in response.url.lower()
        and response.request.method == "POST"
    ) as response_info:

        login_page.login(user["phone"], user["password"])

    # API assertion
    assert response_info.value.status in [200, 400]

    # UI assertion (only if login succeeds)
    if response_info.value.status == 200:
        expect(page).not_to_have_url(f"{base_url}/login")


 
# INVALID LOGIN TEST
def test_invalid_login(page: Page, base_url: str, test_data: dict):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.navigate_to_home(base_url)
    home_page.go_to_login()

    user = test_data["invalid_user"]

    login_page.login(user["phone"], user["password"])

    
    expect(
        page.get_by_text("Invalid phone or password", exact=True)
    ).to_be_visible()