import requests
import pytest


def brewery_id_generator():
    response = requests.get('https://api.openbrewerydb.org/v1/breweries')
    for el in response.json():
        yield el['id']


brewery_id_gen = brewery_id_generator()


def brew_cities():
    resp = requests.get('https://api.openbrewerydb.org/v1/breweries')
    cities = []
    for el in resp.json():
        if el['city'] not in cities:
            cities.append(el['city'])
    return cities
