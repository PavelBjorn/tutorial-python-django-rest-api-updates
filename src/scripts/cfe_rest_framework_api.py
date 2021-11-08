import requests
import json
import os
from random import random

ENDPOINT = "http://127.0.0.1:8000/api/status/"
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
REFRESH_AUTH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

token = None


def create_user():
    global token
    register_headers = {
        "content-type": "application/json"
    }
    register_data = {
        'username': str(input("User Name: ")).strip(),
        'email': str(input("Email: ")).strip(),
        'password': str(input("Password: ")).strip(),
        'password2': str(input("Repeate Password: "))
    }
    r_register = requests.post(AUTH_ENDPOINT + "register/", data=json.dumps(register_data), headers=register_headers)
    print("Register -> " + r_register.text)


def get_token():
    global token
    if token is None:
        auth_headers = {
            "content-type": "application/json"
        }
        auth_data = {
            'username': str(input("User Name/Email: ")).strip(),
            'password': str(input("Password: ")).strip()
        }
        r_auth = requests.post(AUTH_ENDPOINT, data=json.dumps(auth_data), headers=auth_headers)
        print("Auth -> " + r_auth.text)
        token = r_auth.json()['token']

    return token


def refresh_token(token):
    refresh_data = {
        'token': token
    }
    r_auth_refresh = requests.post(REFRESH_AUTH_ENDPOINT, data=json.dumps(refresh_data), headers=auth_headers)
    refresh_token = r_auth_refresh.json()['token']
    print("Refresh Token -> " + refresh_token)
    return refresh_token


# TODO detect how to send multipart data to make put method works
def do(token, method='get', id=None, data={}, image_path=None):
    headers = {
        "Authorization": "JWT " + token,
    }
    if image_path is None:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)

    print(image_path)

    url = ENDPOINT
    if id is not None:
        url = url + id + "/"

    print(url)
    if image_path is not None:
        with open(image_path.replace("\"", ""), mode="rb") as image:
            fileData = {
                'image': image
            }
            r = requests.request(method, url, data=data, files=fileData, headers=headers)
    else:
        r = requests.request(method, url, data=data, headers=headers)

    print("Url: " + r.url)
    print("Status code:" + str(r.status_code))
    print(r.text)
    return r


def executeRequest():
    request_type = str(input("Request Type register/get/get_item/put/post/put_image/post_image/exit: ")).strip()
    if request_type == "get":
        do(token=get_token(), method="get")
    elif request_type == "get_item":
        do(token=get_token(), method="get", id=str(input("Item Id: ")))
    elif request_type == "put":
        do(token=get_token(), method="put", id=str(input("Item Id: ")), data={"content": str(input("Content: "))})
    elif request_type == "put_image":
        do(token=get_token(), method="put", id=str(input("Item Id: ")), image_path=input("Image path: "))
    elif request_type == "post":
        do(token=get_token(), method="post", data={"content": str(input("Content: "))})
    elif request_type == "post_image":
        do(token=get_token(), method="post", image_path=input("Image path: "))
    elif request_type == "register":
        create_user()
    elif request_type == "exit":
        print("Exit from script")
        return
    else:
        print(request_type + " is wrong type of request!!! get/get_item/put/post/put_image/post_image/exit allowed")

    executeRequest()


executeRequest()
