﻿import os
import unittest
from unittest.mock import MagicMock, patch
from app.flask_app import create_app
from app.file_manager import save_file

class RoutesTests(unittest.TestCase):
    def setUp(self):
        # Create a dummy GoogleSearcher with a search method returning a known value.
        self.google_scrapper_mock = MagicMock()
        self.google_scrapper_mock.search.return_value = [
            {'title': 'Test Title', 'link': 'http://example.com'}
        ]
        self.app = create_app(self.google_scrapper_mock)
        self.client = self.app.test_client()

    def test_index_route(self):
        template_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'templates', 'index.html')
        with open(template_path, encoding='utf-8-sig') as f:
            expected_html = f.read().strip()

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        actual_html = response.data.decode('utf-8-sig').strip()
        self.assertMultiLineEqual(actual_html, expected_html)

    @patch('app.flask_routes.save_file')
    def test_search_route(self, mock_save_file):
        mock_save_file.return_value = None
        response = self.client.post('/search', data={'query': 'dummy'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data, {'filename': 'dummy.json', 'results': [{'link': 'http://example.com', 'title': 'Test Title'}]})
        self.google_scrapper_mock.search.assert_called_once_with('dummy')

if __name__ == '__main__':
    unittest.main()