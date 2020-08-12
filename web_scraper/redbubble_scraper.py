#This script should gather all design metadata
from urllib.request import urlopen
from bs4 import BeautifulSoup 
from selenium import webdriver

#Using a headless chrome
#***IMPORTANT*** Need to change path for your local machine 
PATH = "/mnt/c/Users/angry/desktop/redbubbleScraper/web_scraper/chromedriver.exe"
driver = webdriver.Chrome(PATH)
#URL to the explore designs page
url_to_scrape = "https://www.redbubble.com/people/S0ULGROUPSTUDIO/explore"
#Open the page
driver.get(url_to_scrape)
#Read page
html = driver.page_source
#Close the page
driver.quit()



#Parse the html
html_soup = BeautifulSoup(html, 'html.parser')
#Target data 
design_card_links = html_soup.findAll("a", class_="styles__link--2sYi3")
design_card_images = html_soup.findAll("img", class_="styles__image--2CwxX styles__rounded--1lyoH styles__fluid--3dxe-")
design_card_names = html_soup.findAll("span", class_="styles__box--206r9 styles__text--NLf2i styles__display6--uq_8G styles__nowrap--2Vk3A styles__display-block--2XANJ")

#URL
"""for link in design_card_links:
    #Design URL
    print(link)
    design_url = link.get('href')
    print("URL: ", design_url)"""
#Image source
"""for image in design_card_images:
    design_photo_url = design_photo.get('src')
    print(design_photo_url)"""
#Design name    
"""for name in design_card_names:
    print(name.txt)"""