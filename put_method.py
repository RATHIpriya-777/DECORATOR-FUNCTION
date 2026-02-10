import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


# ---------- PUT METHOD ----------
def update_post_put(post_id):
    data = {
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/{post_id}", json=data)
    print("PUT Status:", response.status_code)
    print(response.json())


