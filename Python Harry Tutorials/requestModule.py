import requests
from bs4 import BeautifulSoup

# response = requests.get("https://www.google.com")
# print(response.text)

url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": "Shubham",
#     "body": "Angu",
#     "userId": "1"
# }

# headers = {
#     'Content-type': 'application/json; charset=UTF-8',
#   }

# response = requests.post(url,headers=headers,json=data)

# print(response.text)

# this is used for web scrapping

response = requests.get("https://jsonplaceholder.typicode.com/guide/")

soup = BeautifulSoup(response.text,"html.parser")
print(soup.prettify())