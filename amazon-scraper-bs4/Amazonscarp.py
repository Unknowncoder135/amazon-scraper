from numpy.lib.shape_base import get_array_prepare
import pandas as pd
from sys import version
from bs4 import BeautifulSoup
import requests
import random
from bs4 import SoupStrainer


main_list=[]
g=0
search_term = 'headphone'
for z in range(1,15):
    # https://www.amazon.in/s?k=phone&page=2
    url =f'https://www.amazon.in/s?k={search_term}&page={z}'
    print(url)
    headers = {'yout user agent...'}
    r = requests.get(url,headers=headers)
    soup  = BeautifulSoup(r.text,'html.parser')

    name  = soup.find_all('span',class_='a-size-medium a-color-base a-text-normal')
    price = soup.find_all('span',class_='a-price-whole')

    data = soup.find_all('div',class_='a-row a-size-base a-color-secondary s-align-children-center')
    rateings = soup.find_all('span',class_='a-icon-alt')
    imgs = soup.find_all('img',class_='s-image')
    for x in range(0,len(name)):
        title  = name[x].text
        try:
            mal = price[x].text
        except:
            mal = 'no_price'
        try:
            product_data = data[x].text
            rateing = rateings[x].text
            img = imgs[x]['src']
        except:
            product_data = 'none'
            rateing = 'none'
            img = 'Img_link_not_found'
        main_dir = {
            'product_name':title,
            'product_price':mal,
            'product_data':product_data,
            'product_rateing':rateing,
            'img_link':img
        }
        main_list.append(main_dir)
    print(f'printing_page {z}')


# print(don)
# print(main_list)
h = random.randrange(2,100)
data_frame = pd.DataFrame(main_list)

data_frame.to_csv(f'Amazon_data{h}.csv',index=False)
