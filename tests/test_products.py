import pytest
import re
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.product_page import ProductPage

@pytest.mark.regression
def test_browse_category_and_view_product(page: Page, base_url: str):
    """Test navigating through a category to a product details page."""
    home_page = HomePage(page)
    product_page = ProductPage(page)
    
    home_page.navigate_to_home(base_url)
    
    home_page.open_category("Kéwi bags")
    
    expect(page).to_have_url(re.compile(r".*kewi.*"))
    
    home_page.open_first_product()
    
    product_page.assert_element_visible(product_page.add_to_cart_btn)
    assert len(product_page.get_product_title()) > 0, "Product title should not be empty"
