import unittest
from unittest.mock import MagicMock
from app.google_scraper import GoogleScraper

class GoogleScrapperTests(unittest.TestCase):
    def test_search_parses_results(self):
        # Prepare
        sample_html = '''
            <html>
              <body>
                <div class="g">
                  <h3>Test Title 1</h3>
                  <a href="http://example.com/1">Link1</a>
                </div>
                <div class="g">
                  <h3>Test Title 2</h3>
                  <a href="http://example.com/2">Link2</a>
                </div>
              </body>
            </html>
            '''
    
        page_mock = MagicMock()
        page_mock.content.return_value = sample_html
    
        browser_manager_mock = MagicMock()
        browser_manager_mock.new_page.return_value = page_mock
    
        # Exec
        google_searcher = GoogleScraper(browser_manager_mock)
        results = google_searcher.search("test query")
        expected = [
            {'title': 'Test Title 1', 'link': 'http://example.com/1'},
            {'title': 'Test Title 2', 'link': 'http://example.com/2'}
        ]
    
        # Assert
        self.assertEqual(results, expected)

if __name__ == '__main__':
    unittest.main()