import requests
post_url = "https://jsonplaceholder.typicode.com/posts"

weather_data = {
    "city": "Pune",
    "temperature": 20,
    "humidity": 60,
    "Condition": "sunny"
}

response = requests.post(post_url, json=weather_data)
if response.status_code == 201:
    print("Successful Creation")
