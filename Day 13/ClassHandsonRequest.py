import requests




try:
    # Send a request
    response = requests.get("https://restcountries.com/v3.1/all?fields=name,capital,currencies,area,region")
    # response.raise_for_status()

    # Check the status code
    if response.status_code == 200:
        print("Response received")
        print(response.json())
        print('\n')
    else:
        print("Failed to retrieve data. Error code: ", response.status_code)

    countries = response.json()
    # print(countries)

    # Loop through the lists of countries and display relevant information
    def display_data(r, cc):
        for country in countries:
            name = country.get('name', {}).get('common', 'N/A')
            capital = country.get('capital', ['N/A'])
            area = country.get('area', 'N/A')
            currency = country.get('currencies', {})
            region = country.get('region', ['N/A'])

            if region == r.capitalize() and cc.upper() == list(currency.keys())[0]:
                print(f"Country: {name}")
                print(f"Capital: {capital[0]}")
                print(f"Area:    {area}")
                print(f"Region:  {region}")
                print(f"Currency: {currency}")
                print(f"Currency Name: {currency[list(currency.keys())[0]]['name']}")
                print(f"Currency Code: {list(currency.keys())[0]}")
                print(f"Currency symbol: {currency[list(currency.keys())[0]]['symbol'][0]}")


except:
    # if response.status_code == 404:
    if response.status_code == 404:
        print("Hello 404 occurred")
    elif response.status_code == 401:
        print("Error 401 occurred. Unauthorized access.")
    elif response.status_code == 403:
        print("Error 403 occurred. Forbidden.")
    elif response.status_code == 500:
        print("Error 500 occurred. Internal Server Error")


if __name__ == '__main__':
    r = input("Input the region: ")
    cc = input("Input the currency code: ")

    display_data(r, cc)

