import pytest
import re
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.mark.smoke
def test_add_product_to_cart(page: Page, base_url: str):
    """Test adding a product to the cart from the home page."""
    home_page = HomePage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    
    home_page.navigate_to_home(base_url)
    
    home_page.open_first_product()
    
    product_name = product_page.get_product_title()
    
    product_page.add_to_cart()
    product_page.wait_for_success_message()
    
    home_page.go_to_cart()
    cart_page.verify_on_cart_page()
    
