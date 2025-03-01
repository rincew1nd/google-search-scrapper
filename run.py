from app import create_app
from app.browser_manager import BrowserManager
from app.google_scraper import GoogleScraper

if __name__ == '__main__':
    browser_manager = BrowserManager()
    google_searcher = GoogleScraper(browser_manager)
    app = create_app(google_searcher)
    
    try:
        app.run(host='0.0.0.0', port=5394, threaded=False, use_reloader=False)
    finally:
        browser_manager.close()