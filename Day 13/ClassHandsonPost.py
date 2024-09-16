import requests
post_url = "https://reqres.in/api/users"

post_data = {
    "name": "John doe",
    "job": "Software developer"
}

response = requests.post(post_url, json=post_data)
if response.status_code == 201:
    print("Successful Creation")
