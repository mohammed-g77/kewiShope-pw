from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.search_input = "input[placeholder='Search products...']"
        self.cart_icon = "a[href='/cart']"
        # The login icon is the profile icon in the header. We can also just use the href if it was an 'a' tag, 
        # but since it's a button, we can locate it relative to the cart icon or using nth.
        # Since cart is a[href='/cart'], the profile is likely the button right before it.
        self.login_icon = "button.btn-scale:has(svg)"
        self.categories_section = "text=What are you shopping for today?"
        
    def navigate_to_home(self, base_url: str):
        """Navigate to the home page."""
        self.navigate(f"{base_url}/products")
        
    def search_for_product(self, product_name: str):
        """Enter a product name in the search bar and press enter."""
        self.fill(self.search_input, product_name)
        self.page.keyboard.press("Enter")
        
    def go_to_cart(self):
        """Click the cart icon to navigate to the cart page."""
        self.click(self.cart_icon)
        
    def go_to_login(self):
        """Click the login icon to navigate to the login page."""
        # Click the 4th button in the header (Profile icon)
        self.page.locator(self.login_icon).nth(3).click()

    def open_category(self, category_name: str):
        """Click on a category by its name (e.g., 'Kéwi bags')."""
        self.click(f"button:has-text('{category_name}')")
        
    def open_first_product(self):
        """Click on the first product in the product grid."""
        self.page.locator('a[href^="/product/"]').first.click()
