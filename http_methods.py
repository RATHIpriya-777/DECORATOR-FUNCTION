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


# ---------- POST METHOD ----------
def create_post():
    data = {
        "title": "My New Post",
        "body": "This post is created using Python",
        "userId": 1
    }
    response = requests.post(BASE_URL, json=data)
    print("POST Status:", response.status_code)
    print(response.json())


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


# ---------- PATCH METHOD ----------
def update_post_patch(post_id):
    data = {
        "title": "Partially Updated Title"
    }
    response = requests.patch(f"{BASE_URL}/{post_id}", json=data)
    print("PATCH Status:", response.status_code)
    print(response.json())


# ---------- DELETE METHOD ----------
def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/{post_id}")
    print("DELETE Status:", response.status_code)


# ---------- RUN METHODS ----------
if __name__ == "__main__":
    get_posts()
    get_post_by_id(1)
    create_post()
    update_post_put(1)
    update_post_patch(1)
    delete_post(1)