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
# print(mobilelink) 
# print(len(mobilelink))
for links in mobilelink[:2]:
    print(links)
    all_data = {}
    rone = requests.get(links, headers=headers).text
    soupone = BeautifulSoup(rone,'lxml')

    for table in soupone.find_all('table','table table-striped'):
        # print(table)
    # iterating every tr of each table
        temp_heading = ''
        temp_title = []
        for t in table:
            heading = unicodedata.normalize("NFKD",t.th.text)
            title = unicodedata.normalize("NFKD",t.td.text)
          
            if len(heading.strip()) < 1:
                heading = temp_heading
                temp_title.append(title)
                all_data[heading] = temp_title
                
            else:
                temp_title = []
                heading = unicodedata.normalize("NFKD",t.th.text)
                temp_heading = heading
                temp_title.append(title)
                all_data[heading] = title

    list_of_products.append(all_data)
    # print(all_data) 
# print(mobilelink)
print(list_of_products)

with open("sample_product_info.json", "w") as write_file:
    json.dump({"Products": list_of_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))

