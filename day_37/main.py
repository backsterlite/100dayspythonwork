import requests
from bs4 import BeautifulSoup
from datetime import date
USER_NAME = "backster"
PIXE_END_POINT = "https://pixe.la/"
TOKEN = "24c8363d-92cc-4300-934a-4ce5647b0a23"
USER_END_POINT = f"{PIXE_END_POINT}@{USER_NAME}"
CREATE_USER = "v1/users"
CREATE_GRAPH = "/graphs"

headers = {
    "X-USER-TOKEN": TOKEN,
}
user_response = requests.get(USER_END_POINT)
response_html = BeautifulSoup(user_response.text, 'html.parser')

if '404' in response_html.title.text.strip():
    user_is_create = False
    user_params = {
        "token": TOKEN,
        "username": USER_NAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    while not user_is_create:
        response = requests.post(PIXE_END_POINT+CREATE_USER, json=user_params)
        print(response.text)
        user_is_create = bool(response.json()['isSuccess'])
else:
    print("USER ALREADY CREATED")

# Create graph

graph_params = {
    "id": "running128",
    "name": "Running",
    "unit": "kilometer",
    "type": "float",
    "color": "momiji",
    "timezone": "Europe/Kiev"
}
graph_request_str = f"{PIXE_END_POINT}{CREATE_USER}/{USER_NAME}{CREATE_GRAPH}"
print(graph_request_str)

graph_response = requests.post(graph_request_str, json=graph_params, headers=headers)
print(graph_response.text)


# PIXEL CREATE
today = date.today()
today_str = today.strftime("%Y%m%d")
pixel_request_str = f"{PIXE_END_POINT}{CREATE_USER}/{USER_NAME}{CREATE_GRAPH}/{graph_params['id']}"
pixel_params = {
    "date": today_str,
    "quantity": "5.8",
}

pixel_response = requests.post(pixel_request_str, json=pixel_params, headers=headers)
print(pixel_response.text)