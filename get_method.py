import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# ---------- GET METHOD ----------
def get_posts():
    response = requests.get(BASE_URL)
    print("GET Status:", response.status_code)
    print(response.json()[:2])  # show only first 2 posts


# ---------- GET by ID ----------
def get_post_by_id(post_id):
    response = requests.get(f"{BASE_URL}/{post_id}")
    print("GET by ID Status:", response.status_code)
    print(response.json())


