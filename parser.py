import requests
from bs4 import BeautifulSoup

import json

headers = {
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

def get_data(url):
    req = requests.get(url=url, headers=headers)
    src = req.text
    
    soup = BeautifulSoup(src, 'lxml')
    cards = soup.find_all(class_="catalog__product-catalog")
    # print(cards)
    
    parsed = []
    
    for i in cards:
        card = BeautifulSoup(str(i), 'lxml')
        name = card.find(class_='product-card__info--title').text
        sizes = card.find(class_='product-card__info--sizes').text
        price = card.find(class_='product-card__info--price').text
        old_price = card.find(class_='product-card__info--oldprice').text
        print(name, sizes, price, old_price)
    
get_data()
    