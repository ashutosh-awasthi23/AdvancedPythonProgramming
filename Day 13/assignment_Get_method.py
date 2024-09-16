import requests
response = requests.get('https://restcountries.com/v3.1/all')

def regionCountryCode():
    if response.status_code == 200:
        print("Response received")
        print(response.json())
    else:
        print("Failed to retrieve data. Error code: ", response.status_code)

    countries = response.json()
    name = country.get('name', {}).get('common', 'N/A')
    capital = country.get('capital', ['N/A'])[0]
    area = country.get('area', 'N/A')