import os
from playwright.sync_api import sync_playwright

class BrowserManager:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self._get_browser()

    def _get_browser(self):
        # Choose the browser and mode based on the HEADLESS env variable.
        if os.getenv('HEADLESS', 'True') == 'True':
            return self.playwright.firefox.launch(headless=True)
        else:
            return self.playwright.chromium.launch(headless=False)

    def new_page(self):
        return self.browser.new_page()

    def close(self):
        self.browser.close()
        self.playwright.stop()