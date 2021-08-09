import requests
from bs4 import BeautifulSoup

URL = "https://www.flipkart.com/laptops/pr?sid=6bo,b5g&marketplace=FLIPKART"
page = requests.get(URL)
soup = BeautifulSoup(page.content,"html.parser")

specs = ['processor','ram','os','rom','screen','extras','warranty']


def scrap_data():
    laptop_names = []
    prices = []
    ratings = []
    discounts = []
    features_list = []
    for tag in soup.find_all("div",attrs={"class":"_2kHMtA"}):
        laptop_name = tag.find("div",attrs={'class':'_4rR01T'}).text        #1
        price = tag.find("div",attrs={'class':'_30jeq3 _1_WHN1'}).text      #2
        is_rating = tag.find("div",attrs={'class':'_3LWZlK'})
        if is_rating:
            rating = is_rating.text                                         #3
        is_discount = tag.find("div",attrs={"class":"_3Ay6Sb"})
        if is_discount:
            discount = is_discount.text                                     #4
        details_card = tag.find("div",attrs={"class":"fMghEO"})
        laptop_details = details_card.find("ul",attrs={"class":"_1xgFaf"})
        features = {}
        counter = 0
        for lappy in laptop_details:
            data = lappy.text                                               #5,6,7,8,9,10,11
            features[specs[counter]] = data
            counter += 1
        
        laptop_names.append(laptop_name)
        prices.append(price)
        ratings.append(rating)
        discounts.append(discount)
        features_list.append(features)
    
    parsed_data = [laptop_names,prices,ratings,discounts,features_list]
    return parsed_data


if __name__ == '__main__':
    print('Please execute StoreData.py file')

'''
print(laptop_names)
print(prices)
print(ratings)
print(discounts)
print(features_list)
'''
