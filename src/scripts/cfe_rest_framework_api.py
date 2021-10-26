import requests
import json
import os

ENDPOINT = "http://127.0.0.1:8000/api/status/"
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
REFRESH_AUTH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

# AUTH
auth_headers = {
    "content-type": "application/json"
}
auth_data = {
    'username': str(input("User Name: ")),
    'password': str(input("Password: "))
}
r_auth = requests.post(AUTH_ENDPOINT, data=json.dumps(auth_data), headers=auth_headers)
token = r_auth.json()['token']
print("Auth -> " + token)
# Refresh

refresh_data = {
    'token': token
}
r_auth_refresh = requests.post(REFRESH_AUTH_ENDPOINT, data=json.dumps(refresh_data), headers=auth_headers)
refresh_token = r_auth_refresh.json()['token']
print("Refresh Token -> " + refresh_token)

# OTHER
get_data = ENDPOINT + str(22) + "/"

r = requests.get(get_data)
print("R -> " + str(r.text))

r2 = requests.get(ENDPOINT)
print("R2 -> " + str(r2.status_code))

post_data = json.dumps({"content": "Some random content"})
post_headers = {
    "content-type": "application/json"
}
post_response = requests.put(get_data, data=post_data, headers=post_headers)
print("POST respose -> " + str(post_response.text))

# # TODO detect hoe to send multipart data to make put method works
# def do(method='get', id=None, data={}, is_json=True, image_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#
#     print(image_path)
#
#     url = ENDPOINT
#     if id is not None:
#         url = url + id + "/"
#
#     print(url)
#     if image_path is not None:
#         with open(image_path, mode="rb") as image:
#             fileData = {
#                 'image': image
#             }
#             r = requests.request(method, url, data=data, files=fileData)
#     else:
#         r = requests.request(method, url, data=data, headers=headers)
#
#     print("Url: " + r.url)
#     print(r.status_code)
#     print(r.text)
#     return r
#
#
# do(method="put", id='21', data={'user': 1, "conten": "Content With Image"}, is_json=False, image_path=input("Image path: "))

# do(method="put", id='1', data={'user': 1, "content": "try to update content"}, is_json=True)


# do(method="get", id='1')

# do(method='post', data={'user': 1, 'content': "Some new Content"}, image_path=input("Image path: "), is_json=False)
# do(method='put', data={'user': 1, 'content': 'Updated content from script'})
# do(method='delete', data={'id': 12})
# do(method='get')
