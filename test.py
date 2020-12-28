# from bs4 import BeautifulSoup
# import requests
# import json
# import unicodedata


# headers = {
#         'authority': 'www.gsmarena.com.bd',
#         'pragma': 'no-cache',
#         'cache-control': 'no-cache',
#         'dnt': '1',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'sec-fetch-site': 'none',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-dest': 'document',
#         'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#     }


# brands_link = []

# mobilelink = []
# url = 'https://www.gsmarena.com.bd/brands'
# r = requests.get(url, headers=headers).text
# soup = BeautifulSoup(r,'html.parser')



# brand_div = soup.find_all('div', class_='product-thumb')
# for link in brand_div:
#     ab = link.find('a')
#     brands_link.append(link.a['href'])
# for u in brands_link:
#     for x in range(1,4):
#         r = requests.get(u+str(x), headers=headers).text
#         soup_m = BeautifulSoup(r,'html.parser')

#     for link in soup_m.find_all('div','col-xs-6 col-sm-4 col-md-3'):
#         mobilelink.append(link.a['href'])
x = ['sfs','fsd','fss','trdf','hhg','nhnf']
print(x[2:4])