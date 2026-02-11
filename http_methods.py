import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def do(method, id=None, data=None):
    url = BASE_URL

    if id is not None:
        url = f"{BASE_URL}/{id}"

    if method == "GET":
        response = requests.get(url)

    elif method == "POST":
        response = requests.post(url, json=data)

    elif method == "PUT":
        response = requests.put(url, json=data)
    elif method== "PATCH":
        response = requests.patch(url,json=data)

    elif method == "DELETE":
        response = requests.delete(url)

    else:
        print("Invalid method")
        return

    print("Status Code:", response.status_code)

    if response.content:
        print("Response:", response.json())
do("GET")
do("GET", id=1)
do("POST", data={"title": "Hi", "body": "Hello", "userId": 1})
do("PUT", id=1, data={"title": "HI  ALL", "body": "HELLO WORLD", "userId": 1})
do("PATCH", id=1, data={"title": "HI TO ALL", "body": "HELLO WORLD", "userId": 1})
do("DELETE", id=1)