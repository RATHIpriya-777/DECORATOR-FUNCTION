import requests

# The URL for the POST method as seen in your image
url = 'https://jsonplaceholder.typicode.com/posts'

# The data you want to send (must be a dictionary)
my_data = {
    'title': 'Hello World',
    'body': 'This is my first post from VS Code!',
    'userId': 1
}

# Sending the POST request
response = requests.post(url, json=my_data)

# Checking the result
if response.status_code == 201:
    print("Success! Created post:")
    print(response.json())
else:
    print(f"Failed with status code: {response.status_code}")
    
    