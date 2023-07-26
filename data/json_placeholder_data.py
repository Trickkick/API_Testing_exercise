import requests


def base_data():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    i = 1
    for el in response.json():
        data = {
            'title': el['title'] + 'AAA',
            'body': el['body'] + 'BBB',
            'userId': int(el['userId']) + 1,
            'id': i,
        }
        i += 1
        yield data


placeholder_data = base_data()
placeholder_data2 = base_data()

numb_generator = (i for i in range(1, 50))
