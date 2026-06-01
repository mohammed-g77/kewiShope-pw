# pyrefly: ignore [missing-import]
import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage

@pytest.mark.smoke
def test_homepage_elements_load(page: Page, base_url: str):
    """Test that the homepage loads and essential elements are visible."""
    home_page = HomePage(page)
    home_page.navigate_to_home(base_url)
    
    import re
    # Validate title
    expect(page).to_have_title(re.compile(r"Kewi Store.*")) # Adjust based on actual title
    
    # Validate categories section
    home_page.assert_element_visible(home_page.categories_section)
    
    # Validate search bar is present
    home_page.assert_element_visible(home_page.search_input)

def test_search_functionality(page: Page, base_url: str):
    """Test the search bar functionality."""
    home_page = HomePage(page)
    home_page.navigate_to_home(base_url)
    
    home_page.search_for_product("bag")
    
    # Assert that the search results grid is visible after searching
    expect(page.locator(".grid")).to_be_visible()
