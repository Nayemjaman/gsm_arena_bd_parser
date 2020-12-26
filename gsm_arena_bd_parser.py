from bs4 import BeautifulSoup
import requests
import json
import unicodedata


headers = {
        'authority': 'www.gsmarena.com.bd',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

url = 'https://www.gsmarena.com.bd/samsung/'
r = requests.get(url, headers=headers).text
soup = BeautifulSoup(r,'html.parser')

list_of_products = []
mobilelink = []
for link in soup.find_all('div','col-xs-6 col-sm-4 col-md-3'):

    mobilelink.append(link.a['href'])
print(mobilelink[:5]) 