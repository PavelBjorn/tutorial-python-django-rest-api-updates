import requests
import json
from typing import Final

BASE_URL: Final = "http://127.0.0.1:8000/"

ENDPOINT: Final = "api/updates/"


def get_list():
    id = str(input("Enter update id or jut skip it to get list: "))

    if id is None or id == "":
        query = None
    else:
        query = json.dumps({"id": id})

    print(id)
    r = requests.get(BASE_URL + ENDPOINT, data=query)
    data = r.json()
    print(type(json.dumps(data)))

    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


def create_update():
    new_data = {
        "user": int(input("Enter user id: ")),
        "content": str(input("Enter content: "))
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print("Status Code: " + str(r.status_code))

    if r.status_code == requests.codes.ok:
        return r.json()

    return r.text


def do_obj_update():
    new_data = {
        "id": str(input("Please input id: ")),
        "content": str(input("Please enter content: "))
    }
    r = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print("Status Code: " + str(r.status_code))

    if r.status_code == requests.codes.ok:
        return r.json()

    return r.text


def do_obj_delete():
    new_data = {
        "id": str(input("Please input id: "))
    }
    r = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print("Status Code: " + str(r.status_code))

    if r.status_code == requests.codes.ok:
        return r.json()

    return r.text


def execute():
    command = str(input("Please enter command:"))
    try:
        if command == "del":
            result = do_obj_delete()
        elif command == "create":
            result = create_update()
        elif command == "update":
            result = do_obj_update()
        elif command == "get":
            result = get_list()
        else:
            result = "Unknown command " + command

        print(result)
    except Exception as e:
        print(e)
        execute()


execute()
