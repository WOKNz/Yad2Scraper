#%% Imports
from bs4 import BeautifulSoup
import requests
from requests import get
import time
import random
import os

#%%
#base_url = 'https://www.yad2.co.il/realestate/rent?city=4000&page='
base_folder = 'haifa_2021_02_23/'
houses = []
count = 3
entries = os.listdir('haifa_2021_02_23/')

for html_file in entries:
    # url = base_url + str(count)
    # response = get(entries,headers=headers)
    # with open("response.html", "wb") as f:
    #     f.write(response.content)

    # with open(base_folder + html_file, 'r') as f:
    #     contents = f.read()

    html_soup = BeautifulSoup(open(base_folder + html_file, encoding="utf8"), 'html.parser')

    house_data = html_soup.find_all('div', class_="feeditem table")
    if house_data != []:
        houses.extend(house_data)
        # value = random.random()
        # scaled_value = 15+5*value
        # print('Wait ' + str(scaled_value)+'s')
        # time.sleep(scaled_value)

print("Done!")
#%%
import pandas as pd

columns = ['type','neighborhood','city',\
    'street','rooms','floor','size','price','img','id']

count = 1
for apartment in houses:
    
    find1 = apartment.findAll("span", class_="val")
    rooms = find1[0].text
    floor = find1[1].text
    size = find1[2].text
    
    find2 = apartment.findAll("span", class_="title")
    street = find2[0].text
   
    find3 = apartment.findAll("span", class_="subtitle")
    type_nb_city = find3[0].text
    type_nb_city_list = type_nb_city.split(', ')

    apr_type = type_nb_city_list[0]
    neighborhood = type_nb_city_list[1]
    city = type_nb_city_list[2]

    find4 = apartment.findAll("div", class_="price")
    price = find4[0].text
    price = "".join(filter(str.isdigit, price))

    find5 = apartment.findAll("img", class_="feedImage")
    img = find5[0]['src']

    find6 = apartment.findAll("div", class_="feed_item feed_item-v4 accordion desktop")
    id_str = find6[0]['item-id']

    print(id_str)

    if count == 1:
        break
    count += 1
# %%
print(houses[0])
# %%
