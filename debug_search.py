import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        
        # Track all request URLs
        requests = []
        page.on("request", lambda request: requests.append(request.url))
        
        print("Navigating to https://kewi.ps/products...")
        try:
            await page.goto("https://kewi.ps/products", timeout=45000)
            print("Successfully navigated!")
        except Exception as e:
            print(f"Navigation failed: {e}")
            await browser.close()
            return
        
        # Take an initial screenshot
        await page.screenshot(path="initial_page.png")
        print("Initial screenshot saved to initial_page.png")
        
        # Look for search input and search
        search_input_selector = "input[placeholder='Search products...']"
        try:
            await page.wait_for_selector(search_input_selector, timeout=10000)
            print("Search input found! Typing 'bag' and pressing Enter...")
            await page.fill(search_input_selector, "bag")
            
            # Clear requests list to focus on search requests
            requests.clear()
            
            await page.keyboard.press("Enter")
            # Wait a few seconds for search to complete/network requests to fire
            await page.wait_for_timeout(5000)
            
            await page.screenshot(path="after_search.png")
            print("After search screenshot saved to after_search.png")
            
            print("\nNetwork requests captured during search:")
            for req in requests:
                print(f" - {req}")
        except Exception as e:
            print(f"Search failed: {e}")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
