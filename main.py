import requests
# from tests.dogs_data import breeds_generator
# from tests.dogs_data import sub_breeds_data_generator
from data.brewery_data import brew_cities
import re
from math import sqrt
from data.json_placeholder_data import placeholder_data

"""url = "https://dog.ceo/api/breeds/list/all"

response = requests.get(url)
breeds = response.json()['message']
status = response.json()['status']"""

"""for breed in breeds_generator:
    gen = sub_breeds_data_generator(breed)
    for sub in gen:
        response = requests.get(f"https://dog.ceo/api/breed/{str(sub)}-{str(breed)}/images/random")
        print(response.json()['message'], response.json()['status'], breed, sub)
"""
"""for breed in breeds_generator:
    gg = sub_breeds_data_generator(breed)
    for sub in gg:
        if len(sub) > 0:
            response = requests.get(f"https://dog.ceo/api/breed/{breed}/{sub}/images/random")
            print(f"{response.json()['message']}")
        else:
            response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
            print(f"{response.json()['message']}")
"""
"""text = "https://images.dog.ceo/breeds/retriever-chesapeake/n02099849_1997.jpg"
text = text.split("/")
print(text)"""

"""coord = [38.0, 77.0]
response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_dist={coord[0]},{coord[1]}")
for i in range(1, len(response.json())):
    print(sqrt((float(response.json()[i]['latitude']) - coord[0]) ** 2 + (
            float(response.json()[i]['longitude']) - coord[1]) ** 2) >= sqrt(
        (float(response.json()[i - 1]['latitude']) - coord[0]) ** 2 + (
                float(response.json()[i - 1]['longitude']) - coord[1]) ** 2))"""

"""response = requests.get(f"https://api.openbrewerydb.org/v1/breweries/autocomplete?query=ssd")
for brewery in response.json():
    print(brewery)

res = requests.get("https://api.openbrewerydb.org/v1/breweries/58bc0ff5-5ada-4b37-a5c0-325746773116")
print(res.json())"""

for el in placeholder_data:
    response = requests.post('https://jsonplaceholder.typicode.com/posts', el)
    print(response.json())
