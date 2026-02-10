import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# ---------- DELETE METHOD ----------
def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/{post_id}")
    print("DELETE Status:", response.status_code)


