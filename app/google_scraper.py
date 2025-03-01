from bs4 import BeautifulSoup
from playwright_stealth import stealth_sync
from app.browser_manager import BrowserManager

class GoogleScraper:
    def __init__(self, browser_manager: BrowserManager):
        self.browser_manager = browser_manager

    def search(self, query: str):
        page = self.browser_manager.new_page()
        stealth_sync(page)
        page.goto('http://google.com/')
        page.type('textarea', query)
        page.keyboard.press("Enter")
        page.wait_for_timeout(1000)
        page.wait_for_load_state("domcontentloaded")
        page_content = page.content()
        page.close()
        
        return self.parse_content(page_content)
    
    @staticmethod
    def parse_content(content):
        soup = BeautifulSoup(content, 'html.parser')
        output = []
        for result in soup.select('div.g'):
            try:
                title = result.find('h3').text
                link = result.find('a')['href']
                output.append({'title': title, 'link': link})
            except Exception as e:
                print(f'Error - {e}')
        return output