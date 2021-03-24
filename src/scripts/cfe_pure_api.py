import requests
import json
from typing import Final

BASE_URL: Final = "http://127.0.0.1:8000/"

ENDPOINT: Final = "api/updates/"


def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()
    print(type(json.dumps(data)))
    for obj in data:
        print(obj['id'])
        if obj['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            print(r2.json())
    return r.json()


def create_update():
    new_data = {
        "user": 1,
        "content": "Another use content"
    }
    r = requests.delete(BASE_URL + ENDPOINT, data=new_data)
    print("Status Code: " + str(r.status_code))

    if r.status_code == requests.codes.ok:
        print(r.json())

    return r.text


# get_list()
print(create_update())
