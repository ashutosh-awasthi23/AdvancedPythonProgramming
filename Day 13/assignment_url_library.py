import re
from urllib.parse import urlparse, parse_qs, urlencode

file = open('url.txt', 'r')
p = []
li = file.readlines()
l = []
for i in li:
    l.append(i.replace("\n", ""))

# pattern = r'\b[https?://www\.([a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+)(?/?([a-zA-Z0-9-]+)+)?\??([a-zA-Z0-9-]=[a-zA-Z0-9-])(\&?([a-zA-Z0-9-]=[a-zA-Z0-9-])?)]\b'

for i in l:

    # if re.match(pattern, i):
    #     p.append(i)

    if i.startswith("https") or i.startswith("http"):
        p.append(i[:-1])


print(p)

for i in p:
    parsed_url = urlparse(i)
    print(f"Domain: {parsed_url.netloc}")
    print(f"Path: {parsed_url.path}")
    print(f"Query: {parsed_url.query}")
    print("==========================")
