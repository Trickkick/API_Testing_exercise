import requests
import pytest
from tests.dogs_data import breeds_generator


# from tests.dogs_data import sub_breeds_data_generator


@pytest.mark.parametrize("url", [
    "https://dog.ceo/api/breeds/list/all",
    "https://dog.ceo/api/breeds/image/random",
    "https://dog.ceo/api/breeds/image/random/3",
    "https://dog.ceo/api/breed/hound/images",
    "https://dog.ceo/api/breed/hound/images/random",
    "https://dog.ceo/api/breed/hound/list",
    "https://dog.ceo/api/breed/hound/afghan/images",
    "https://dog.ceo/api/breed/hound/afghan/images/random"
])
def test_dog_api_response_status_positive(url):
    response = requests.get(url)
    assert response.json()['status'] == 'success'
    assert response.ok


def test_dog_api_response_status_negative():
    response = requests.get("https://dog.ceo/api/breeds/list/alll")
    assert response.json()['status'] == 'error'
    assert not response.ok


@pytest.mark.parametrize("breed", breeds_generator)
def test_dog_api_by_breed(breed):
    r = requests.get(f"https://dog.ceo/api/breed/{breed}/list")
    subs = r.json()['message']
    if len(subs) > 0:
        for sub in subs:
            response = requests.get(f"https://dog.ceo/api/breed/{breed}/{sub}/images/random")
            assert response.json()['status'] == 'success'
            assert response.json()['message'].split('/')[4] == f"{breed}-{sub}"
    else:
        response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
        assert response.json()['status'] == 'success'
        assert response.json()['message'].split('/')[4] == breed


def test_dog_api_multiple_random_images():
    for i in range(1, 50):
        response = requests.get(f"https://dog.ceo/api/breeds/image/random/{i}")
        assert response.json()['status'] == 'success'
        assert len(response.json()['message']) == i
