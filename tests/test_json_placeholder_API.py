import pytest
import requests
from data.json_placeholder_data import placeholder_data
from data.json_placeholder_data import placeholder_data2
from data.json_placeholder_data import numb_generator


@pytest.mark.parametrize("numb", numb_generator)
def test_getting_resource(numb):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{numb}')
    assert response.ok


def test_listing_resources():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert len(response.json()) > 1
    for i in range(1, len(response.json())):
        assert response.json()[i]['id'] > response.json()[i - 1]['id']


@pytest.mark.parametrize("data", placeholder_data)
def test_creating_resource(data):
    response = requests.post('https://jsonplaceholder.typicode.com/posts', data)
    assert response.ok
    assert response.json()['id'] is not None
    assert response.json()['title'] == data['title']
    assert response.json()['body'] == data['body']
    assert response.json()['userId'] == str(data['userId'])


@pytest.mark.parametrize("data", placeholder_data2)
def test_updating_resource(data):
    response = requests.put('https://jsonplaceholder.typicode.com/posts/1', data)
    assert response.ok
    assert response.json()['id'] is not None
    assert response.json()['title'] == data['title']
    assert response.json()['body'] == data['body']
    assert response.json()['userId'] == str(data['userId'])


@pytest.mark.parametrize('numb', [
    1,
    5,
    15,
])
def test_delete_resource(numb):
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{numb}')
    assert response.ok


@pytest.mark.parametrize('usId', [
    1,
    2
])
def test_filter_resources(usId):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts?userId={usId}')
    for res in response.json():
        assert res['userId'] == usId
