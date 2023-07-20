import requests
from tests.dogs_data import breeds_generator
#from tests.dogs_data import sub_breeds_data_generator


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
text = "https://images.dog.ceo/breeds/retriever-chesapeake/n02099849_1997.jpg"
text = text.split("/")
print(text)