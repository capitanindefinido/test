import unittest
from unittest.mock import MagicMock, patch
from webScrap import get_url_response, extract_book_info, extract_books_from_page
from bs4 import BeautifulSoup

class TestWebScrapingFunctions(unittest.TestCase):
    
    def test_get_url_response(self):
        url = "https://example.com"
        response = get_url_response(url)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
