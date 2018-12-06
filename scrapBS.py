import requests
from bs4 import BeautifulSoup
import json



cleanHouses = []



# print(house.prettify())
# print('-'*40)



def filter(tag):
    return tag.has_attr('content') and tag.has_attr('itemprop')



for i in range(1,8):

  url = 'https://www.fincaraiz.com.co/casas/venta/bogota/?ad=30|'+str(i)+ '||||1||9|||67|3630001||||||||||||||||1|||1||griddate%20desc||||||'


  page = requests.get(url).content
  soup = BeautifulSoup(page, 'html.parser')
  houses = soup.find_all('ul',class_='advert')

  

  for house in houses:
    
    if 'Product_Code_DON' in house['class']:
      continue
    

    #name
    name = house.find('h2').get_text().strip()

    #price
    uglyPrice = (house.find_all('li',class_='price')[0].find_all(filter)[0].get_text().strip())
    price = int(uglyPrice.split("$")[1].strip().replace('.',''))

    #whole house
    myHouse = {'name':name,'price':price}

    cleanHouses.append(myHouse)


print('Collected data on {} houses'.format(len(cleanHouses)))

with open('data.json', 'w') as outfile:
    json.dump(cleanHouses, outfile)


# print(list(houses[-1].children))
