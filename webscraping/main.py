
import requests 
import random
from bs4 import BeautifulSoup
import csv

    
def scrape_page(soup, quotes):
    for quote_elements in all_quote_elements:
        
        text = quote_elements.find('span', class_='text').text

        author = quote_elements.find('small', class_='author').text

        tag_elements = quote_elements.select('.tags, .tag')


        tags = []
        for tag_element in tag_elements:
            tags.append(tag_element.text)
        
        quotes.append(
            {
                'text' : text,
                'Author' : author,
                'tags' : ', '.join(tags)
            }
        )


home_url = 'https://quotes.toscrape.com/'

headers = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0'
]

headers = {
    'User-Agent' : random.choice(headers)
}

page = requests.get(home_url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

all_quote_elements = soup.find_all('div', class_='quote')

quotes = []

scrape_page(soup, quotes)

next_page = soup.find('li', class_='next')

while next_page is not None:
    next_page_url = next_page.find('a', href=True)['href']
    
    page = requests.get(home_url + next_page_url, headers=headers)

    soup = BeautifulSoup(page.text, 'html.parser')

    scrape_page(soup, quotes)

    next_page = soup.find('li', class_='next')
    print(home_url+next_page_url)

with open('quotes.csv', 'a', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Text', 'Author', 'Tags'])

    for quote in quotes:
        writer.writerow(quote.values())
        
