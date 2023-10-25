import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time

# Función para obtener la respuesta de una URL
def get_url_response(url):
    response = requests.get(url)
    return response

# Función para extraer información de un libro
def extract_book_info(book_soup):
    title = book_soup.find('h1').text
    category = book_soup.find('ul', class_="breadcrumb").find_all('a')[2].text.strip()
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
    return {
        'Title': title,
        'Category': category,
        'Price': price,
        'Stock': stock,
        'Img': img,
        'UPC': upc,
        'Product Type': product_type,
        'Price (excl. tax)': price_excl_tax,
        'Price (incl. tax)': price_incl_tax,
        'Tax': tax,
        'Availability': availability,
        'Number of reviews': number_of_reviews
    }

# Función para extraer información de libros en una página
def extract_books_from_page(url):
    response = get_url_response(url)
    if response:
        soup = BeautifulSoup(response.content, 'html.parser')
        books = soup.find_all('h3')
        books_data = []

        for book in books:
            book_url = book.find('a')['href']
            book_response = get_url_response(urlMain + "catalogue/" + book_url)
            if book_response:
                book_soup = BeautifulSoup(book_response.content, "html.parser")
                book_info = extract_book_info(book_soup)
                books_data.append(book_info)

        return books_data


urlMain = "https://books.toscrape.com/"
urlBase = "https://books.toscrape.com/catalogue/page-{}.html"
all_books_data = []

for page_num in range(1, 51):
    page_url = urlBase.format(page_num)
    books_data = extract_books_from_page(page_url)
    all_books_data.extend(books_data)
    print("***********")
    print(f'{page_num * len(books_data)} libros extraídos...')

df = pd.DataFrame(all_books_data)
df.to_csv("books_scraped1.csv", index=False)
