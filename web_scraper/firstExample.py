from urllib.request import urlopen
from bs4 import BeautifulSoup 

url_to_scrape = "https://planetdesert.com/collections/cactus"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')
cactus_items = html_soup.find_all('div', class_="grid-product__content")

for cactus in cactus_items:
    title = cactus.find('div', class_="grid-product__title").text
    price = cactus.find('div', class_="grid-product__price").text
    print("Title: ",title,"--","Price",price)