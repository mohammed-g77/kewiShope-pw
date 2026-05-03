from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.phone_input = "input[placeholder='Enter your phone number']" # Site uses phone instead of email
        self.password_input = "input[placeholder='Enter your password']"
        self.login_btn = 'button:has-text("Login")'
        self.error_message ="text=Invalid phone or password"
        
    def login(self, phone: str, password: str):
        """Perform login action."""
        self.fill(self.phone_input, phone) 
        self.fill(self.password_input, password)
        self.click(self.login_btn)
        
    def verify_error_message(self):
        self.wait_for_element(self.error_message)
        self.assert_element_visible(self.error_message)