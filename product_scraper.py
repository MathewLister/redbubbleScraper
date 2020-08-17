# This script should gather all design metadata
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def scrape_products(url, file_extension):
    # Using a headless chrome
    PATH = "./chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)

    # Open the page
    driver.get(url)
    # Read page
    html = driver.page_source
    # Close the page
    driver.quit()

    # Parse the html
    html_soup = BeautifulSoup(html, 'html.parser')

    # Target data
    product_card_links = html_soup.findAll("a", class_="styles__link--2sYi3")
    # product_card_images = html_soup.findAll("img", class_="styles__image--2CwxX styles__rounded--1lyoH styles__fluid--3dxe-")
    product_card_names = html_soup.findAll("span", class_="styles__box--206r9 styles__text--NLf2i styles__display6--uq_8G styles__nowrap--2Vk3A styles__display-block--2XANJ")
    product_card_prices = html_soup.findAll("span", class_="styles__box--206r9 styles__text--NLf2i styles__body--3bpp7 styles__display-block--2XANJ")

    # CSV
    filename = ('Products ' + file_extension + '.csv')
    f = open(filename, 'w')
    headers = 'Product Link, Product Name, Product Price \n'
    f.write(headers)

    for link, name, price in zip(product_card_links, product_card_names, product_card_prices):
        product_url = link.get('href')

        f.write(product_url + ',' + (",".join(name.contents)) + ',' + price.text + '\n')

    # Close file
    f.close()
