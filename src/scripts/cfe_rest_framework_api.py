import requests
import json
import os

ENDPOINT = "http://127.0.0.1:8000/api/status/"


def do_img(method='get', data={}, is_json=True, image_path=None):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)

    print(image_path)
    if image_path is not None:
        with open(image_path, mode="rb") as image:
            fileData = {
                'image': image
            }
            r = requests.request(method, ENDPOINT, data=data, files=fileData)
    else:
        r = requests.request(method, ENDPOINT, data=data, headers=headers)

    print(r.status_code)
    print(r.text)
    return r


do_img(method="post", data={'user': 1, "conten": ""}, is_json=False, image_path=input("Image path: "))


def do(method='get', data={}, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)

    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.status_code)
    print(r.text)
    return r

# do(method='post', data={'id':12, 'user': 1, 'content': 'content from script'})
# do(method='put', data={'id': 12,'user': 1, 'content': 'Updated content from script'})
# do(method='delete', data={'id': 12})
# do(method='get')
