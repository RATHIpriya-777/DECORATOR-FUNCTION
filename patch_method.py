import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


# ---------- PATCH METHOD ----------
def update_post_patch(post_id):
    data = {
        "title": "Partially Updated Title"
    }
    response = requests.patch(f"{BASE_URL}/{post_id}", json=data)
    print("PATCH Status:", response.status_code)
    print(response.json())



