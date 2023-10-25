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

















































































""" # Importar librerías
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time
import unittest

urlMain = "https://books.toscrape.com/"
response = requests.get(urlMain)
if response.status_code == 200:
    print("Response successful")
else:
    print("Request failed")

# Extraer detalles de las 50 páginas
books_data = []
for page_num in range(1,51):
    url = f'https://books.toscrape.com/catalogue/page-{page_num}.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extraer los libros y su información de la primera página
    books = soup.find_all('h3')
    start_time = time.time()
    # Iterar en los libros y extraer la información de cada libro
    for book in books:
        # Obtener la url y enviar la peticion GET
        book_url = book.find('a')['href']
        book_response = requests.get(urlMain + "catalogue/" + book_url)
        book_soup = BeautifulSoup(book_response.content, "html.parser")
        title = book_soup.find('h1').text
        category = book_soup.find('ul', class_= "breadcrumb").find_all('a')[2].text.strip()
        price = book_soup.find('p', class_='price_color').text.strip()
        stock = book_soup.find('p', class_='availability').text.strip()
        img = book_soup.find('img')['src']
        upc = book_soup.find('table', class_='table-striped').find_all('tr')[0].find('td').text.strip()
        product_type = book_soup.find('table', class_='table-striped').find_all('tr')[1].find('td').text.strip()
        price_excl_tax = book_soup.find('table', class_='table-striped').find_all('tr')[2].find('td').text.strip()
        price_incl_tax = book_soup.find('table', class_='table-striped').find_all('tr')[3].find('td').text.strip()
        tax = book_soup.find('table', class_='table-striped').find_all('tr')[4].find('td').text.strip()
        availability = book_soup.find('table', class_='table-striped').find_all('tr')[5].find('td').text.strip()
        number_of_reviews = book_soup.find('table', class_='table-striped').find_all('tr')[6].find('td').text.strip()
        end_time = time.time()
        total_time = (end_time-start_time)
        books_data.append([title, category, price, stock, img, upc, product_type, price_excl_tax, price_incl_tax, tax, availability, number_of_reviews])
        print("***********")
        print(f'{page_num * len(books)} libros extraídos...') 

#Exportar data

df = pd.DataFrame(books_data, columns=["Title", "Category", "Price", "Stock", "Img", "UPC", "Product Type", "Price (excl. tax)", "Price (incl. tax)", "Tax", "Availability", "Number of reviews"])

#Guardar en csv
df.to_csv("books_scraped.csv", index=False) """