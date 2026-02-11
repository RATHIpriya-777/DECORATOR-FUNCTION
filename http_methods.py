import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def do(method, id=None, data=None):
    url = BASE_URL

    if id is not None:
        url = f"{BASE_URL}/{id}"

    methods = {
        "GET": requests.get,
        "POST": requests.post,
        "PUT": requests.put,
        "PATCH": requests.patch,
        "DELETE": requests.delete
    }

    request_function = methods.get(method)

    response = request_function(url, json=data)

    print("Status Code:", response.status_code)

    if response.content:
        print("Response:", response.json())


do("GET")
do("GET", id=1)
do("POST", data={"title": "Hi", "body": "Hello", "userId": 1})
do("PUT", id=1, data={"title": "HI ALL", "body": "HELLO WORLD", "userId": 1})
do("PATCH", id=1, data={"title": "HI TO ALL"})
do("DELETE", id=1)
