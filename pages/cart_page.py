from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.checkout_btn = "button:has-text('Checkout')"
        self.cart_items = ".flex.items-center.justify-between.border-b" # Example structure
        self.empty_cart_msg = "text=Your cart is empty"
        self.cart_title = "h1:has-text('Shopping Cart')"
        
    def verify_on_cart_page(self):
        """Assert that the user is on the cart page."""
        self.assert_element_visible(self.cart_title)
        
    def click_checkout(self):
        """Click the checkout button."""
        self.click(self.checkout_btn)
        
    def verify_product_in_cart(self, product_name: str):
        """Verify that a specific product is in the cart."""
        expect(self.page.locator(f"text={product_name}").first).to_be_visible()
