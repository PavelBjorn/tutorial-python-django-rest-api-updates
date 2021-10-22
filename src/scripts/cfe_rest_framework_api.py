import requests
import json
import os

ENDPOINT = "http://127.0.0.1:8000/api/status/"

# TODO detect hoe to send multipart data to make put method works
def do(method='get', id=None, data={}, is_json=True, image_path=None):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)

    print(image_path)

    url = ENDPOINT
    if id is not None:
        url = url + id + "/"

    print(url)
    if image_path is not None:
        with open(image_path, mode="rb") as image:
            fileData = {
                'image': image
            }
            r = requests.request(method, url, data=data, files=fileData)
    else:
        r = requests.request(method, url, data=data, headers=headers)

    print("Url: " + r.url)
    print(r.status_code)
    print(r.text)
    return r


do(method="put", id='21', data={'user': 1, "conten": "Content With Image"}, is_json=False, image_path=input("Image path: "))

# do(method="put", id='1', data={'user': 1, "content": "try to update content"}, is_json=True)


# do(method="get", id='1')

# do(method='post', data={'user': 1, 'content': "Some new Content"}, image_path=input("Image path: "), is_json=False)
# do(method='put', data={'user': 1, 'content': 'Updated content from script'})
# do(method='delete', data={'id': 12})
# do(method='get')
