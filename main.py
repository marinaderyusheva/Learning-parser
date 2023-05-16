import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# запишем веб страницу в файл
URL_TEMPLATE = "https://matrix12.ru/goods/phone/mobilephones/?price%5Bfrom%5D=800&price%5Bto%5D=1000&filter=%ED%E0%E9%F2%E8"
r = requests.get(URL_TEMPLATE)
with open('matrix.html', 'w', encoding='utf-8') as output_file:
  output_file.write(r.text)

soup = bs(r.text, "html.parser")
name = soup.find_all('div', class_='catalog_item_info')
price = soup.find_all('span', class_='editor-pane-num')



for i in range(0, len(price)):
    phone = f"{name[i]}: {price[i]}"
    print(phone)




