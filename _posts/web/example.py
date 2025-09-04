import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")
for link in links:
    print(link.get("href"))

import re
soup = soup.find_all("a", href=re.compile("iana"))

print(soup[0].get('href'))
# def parse_string(text) : 
#     text = text.replace(" ", "").replace("\n", "")
#     return re.sub(r"[^\w\u4e00-\u9fff]", "", text)

# print(parse_string(str(soup)))