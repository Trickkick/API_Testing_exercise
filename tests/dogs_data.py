import requests


def breeds_data_generator():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    breeds = response.json()['message']
    for breed in breeds:
        yield f"{breed}"


breeds_generator = breeds_data_generator()


"""def sub_breeds_data_generator(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/list")
    for el in response.json()['message']:
        yield f"{el}"
"""