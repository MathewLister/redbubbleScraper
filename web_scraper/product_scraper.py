# This script should gather all design metadata
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main(url):
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
    product_card_images = html_soup.findAll("img", class_="styles__image--2CwxX styles__rounded--1lyoH styles__fluid--3dxe-")
    product_card_names = html_soup.findAll("span", class_="styles__box--206r9 styles__text--NLf2i styles__display6--uq_8G styles__nowrap--2Vk3A styles__display-block--2XANJ")
    product_card_prices = html_soup.findAll("span", class_="styles__box--206r9 styles__text--NLf2i styles__body--3bpp7 styles__display-block--2XANJ")

    # URL
    for link in product_card_links:
        # Design URL
        design_url = link.get('href')
        print("URL: ", design_url)
    # Image source
    '''for image in product_card_images:
        design_photo_url = image.get('src')
        print("Photo URL: ", image)'''
    # Design name
    for name in product_card_names:
        print("Product Name: ", name.contents)
    for price in product_card_prices:
        print("Product Price: ", price.contents)


main("https://www.redbubble.com/shop/ap/50235088")
