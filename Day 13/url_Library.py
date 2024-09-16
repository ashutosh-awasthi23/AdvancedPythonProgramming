from urllib.parse import urlparse, parse_qs, urlencode

# Extracting the domain name from a full URL to identify which website is being accessed
print("\nExtracting the domain name from a full URL to identify which website is being accessed:")
url = 'https://www.example.com/pth/to/resource?search=python&lang=en'
parsed_url = urlparse(url)
print(f"Domain: {parsed_url.netloc}")
print(f"Path: {parsed_url.path}")
print(f"Query: {parsed_url.query}")
print("=====================================================")

# Extracting or modifying query parameters in a URL, at runtime
print("\nExtracting or modifying query parameters in a URL, at runtime:")
url = 'https://www.example.com/search?query=python&sort=recent'
parsed_url = urlparse(url)
query_params = parse_qs(parsed_url.query)
print(f"Query Params: {query_params}")
print("=====================================================")

# Adding or removing query parameters from an existing URL.
print("\nAdding or removing query parameters from an existing URL:")
base_url = 'https://www.example.com/search'
query_params = {'query': 'python', 'sort': 'recent'}
updated_url = f"{base_url}?{urlencode(query_params)}"
print(f"Updated URL: {updated_url}")
print("=====================================================")



