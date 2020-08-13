import requests
from bs4 import BeautifulSoup
import re
from prettytable import PrettyTable

site = "https://ih1.redbubble.net/image.{}/ur,shower_curtain_closed,square,600x600.1.jpg"

p = PrettyTable()
p.field_names = ["Name", "Price", "Url"]


def main(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    target = soup.select("img[class*=styles__rounded--1lyoH]")
    imgs = [img.group(1) for img in re.finditer(r'\.(\d+\.\d{4})', r.text)]
    goal = list(dict.fromkeys(imgs))
    for tar, go in zip(target, goal):
        p.add_row([tar['alt'], tar.find_all_next(
            "span")[3].text, site.format(go)])
    print(p)


main("https://www.redbubble.com/shop/shower-curtains/")