# This script should gather all design metadata
from product_scraper import scrape_products
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options


def scrape_designs():
    # Using a headless chrome
    PATH = "./chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)

    # URL to the explore designs page
    url_to_scrape = "https://www.redbubble.com/people/S0ULGROUPSTUDIO/explore"
    # Open the page
    driver.get(url_to_scrape)
    # Read page
    html = driver.page_source
    # Close the page
    driver.quit()

    # Parse the html
    html_soup = BeautifulSoup(html, 'html.parser')

    # Target data
    design_card_links = html_soup.findAll("a", class_="styles__link--2sYi3")
    design_card_names = html_soup.findAll("span", class_="styles__box--206r9 styles__text--NLf2i styles__display6--uq_8G styles__nowrap--2Vk3A styles__display-block--2XANJ ")

    # CSV
    filename = 'Designs.csv'
    f = open(filename, 'w')
    headers = 'Card Link, Design Name \n'
    f.write(headers)

    # Write data to CSV
    i = 1
    for link, name in zip(design_card_links, design_card_names):
        design_url = link.get('href')
        f.write(design_url + ',' + (",".join(name.contents)) + '\n')
        scrape_products(design_url, (str(i) + "-" + datetime.today().strftime('%Y-%m-%d')))
        i += 1
        print("Collecting Data....")

    # Close file
    f.close()


scrape_designs()
