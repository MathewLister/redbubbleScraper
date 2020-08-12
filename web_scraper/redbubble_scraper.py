#This script should gather all design metadata
from urllib.request import urlopen
from bs4 import BeautifulSoup 
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys

#Using a headless chrome
PATH = "./chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)

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
design_card_names = html_soup.findAll("span", class_="styles__box--206r9 styles__text--NLf2i styles__display6--uq_8G styles__nowrap--2Vk3A styles__display-block--2XANJ ")

#URL
for link in design_card_links:
    #Design URL
    design_url = link.get('href')
    print("URL: ", design_url)
#Image source
'''for image in design_card_images:
    design_photo_url = image.get('src')
    print("Photo URL: ", design_photo_url)'''
#Design name    
for name in design_card_names:
    print("Design Name: ", name.txt)