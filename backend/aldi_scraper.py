import asyncio
import time
from pyppeteer import launch

async def main():
    # Launch the browser; headless=True runs it without a visible window.
    # Set headless=False if you want to see what’s happening.
    browser = await launch(headless=False)

    # Open a new page/tab in the browser
    page = await browser.newPage()

    # Navigate to Aldi's website (update the URL if needed)
    await page.goto('https://new.aldi.us/products')
    time.sleep(15)

    # Wait for a specific element to load. Here, we wait for an <h1> element as an example.
    # Adjust the selector based on the actual element you need.
    await page.waitForSelector('h1')

    # Retrieve the complete HTML content of the page
    content = await page.content()
    print(content)

    # Always remember to close the browser after your task is done!
    await browser.close()

# Run the asynchronous main() function using asyncio's event loop
asyncio.run(main())
