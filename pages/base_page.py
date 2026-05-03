from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        """Navigate to a specific URL."""
        self.page.goto(url)

    def click(self, selector: str):
        """Click an element using its selector."""
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        """Fill an input field with text."""
        self.page.fill(selector, text)

    def is_visible(self, selector: str) -> bool:
        """Check if an element is visible."""
        return self.page.is_visible(selector)

    def wait_for_element(self, selector: str):
        """Wait for an element to be visible."""
        self.page.wait_for_selector(selector, state="visible")

    def assert_element_visible(self, selector: str):
        """Assert that an element is visible on the page."""
        expect(self.page.locator(selector)).to_be_visible()
