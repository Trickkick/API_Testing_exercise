import requests
import pytest
from data.brewery_data import brewery_id_gen
from data.brewery_data import brew_cities
import re


@pytest.mark.parametrize("brew_id", brewery_id_gen)
def test_single_brewery_positive(brew_id):
    response = requests.get(f'https://api.openbrewerydb.org/v1/breweries/{brew_id}')
    assert response.ok
    assert response.json()['id'] == brew_id


@pytest.mark.parametrize('brew_id', [
    'dsd',
    'qwegs',
    'afoih',
    123,
])
def test_single_brewery_negative(brew_id):
    response = requests.get(f'https://api.openbrewerydb.org/v1/breweries/{brew_id}')
    assert not response.ok
    assert response.json()['message'] == "Couldn't find Brewery"


def test_list_breweries_count():
    response = requests.get('https://api.openbrewerydb.org/v1/breweries')
    assert response.ok
    assert len(response.json()) > 1


@pytest.mark.parametrize('city', brew_cities())
def test_brewery_by_city(city):
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_city={city}")
    assert response.ok
    for brewery in response.json():
        assert re.search(city, brewery['city']) is not None


@pytest.mark.parametrize('query', ['dog'])
def test_brewery_autocomplete_query(query):
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries/autocomplete?query={query}")
    for brewery in response.json():
        assert re.search(query, brewery['name'], flags=re.IGNORECASE) is not None


"""@pytest.mark.parametrize('coord', [
    [38.0, 77.0],
    [30.0, 80.0]
])
def test_brewery_by_origin_point(coord):
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_dist={coord[0]},{coord[1]}")
    for i in range(1, len(response.json())):
        assert sqrt((float(response.json()[i]['latitude']) - coord[0]) ** 2 + (
                float(response.json()[i]['longitude']) - coord[1]) ** 2) > sqrt(
            (float(response.json()[i - 1]['latitude']) - coord[0]) ** 2 + (
                        float(response.json()[i - 1]['longitude']) - coord[1]) ** 2)"""
