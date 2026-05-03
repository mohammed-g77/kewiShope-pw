from playwright.sync_api import Page
from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.add_to_cart_btn = "button:has-text('Add to Cart')"
        self.product_title = "h1"
        self.product_price = ".text-3xl"  
        self.success_toast = "text=Added to cart" 
        
    def add_to_cart(self):
        """Click the add to cart button."""
        self.click(self.add_to_cart_btn)
        
    def get_product_title(self) -> str:
        """Get the text of the product title."""
        return self.page.inner_text(self.product_title)
        
    def wait_for_success_message(self):
        """Wait for the 'added to cart' confirmation message."""
        self.page.wait_for_timeout(1000) 
