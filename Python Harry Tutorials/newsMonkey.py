import requests
from bs4 import BeautifulSoup
import json
import geocoder
from geopy.geocoders import Nominatim
    
apiKey = "f3a2e397a0224438afa975467addcbe9"
newsUrl = "https://newsapi.org/v2/top-headlines"

# This code is to get country code and search for specific country
# def getCountry():
#     g = geocoder.ip('me')
#     coords = f"{g.latlng[0]},{g.latlng[1]}"
    
#     geolocator = Nominatim(user_agent="my_geopy_app")
#     location = geolocator.reverse(coords)
#     address = location.raw['address']
#     return address["country_code"]

# country = getCountry()

categories = ["business","entertainment","general","health","science","sports","technology"]

print("\nList of news categories\n")
for i,category in enumerate(categories):
    print(f"{i+1}. {category}")

userChoice = int(input("\nEnter category of news you want to search: "))-1
newsCategory = categories[userChoice]

response = requests.get(f"{newsUrl}?category={newsCategory}&apiKey={apiKey}")

news = response.json()

newsArticles = news["articles"]

print(f"\nHeres your latest headlines on {newsCategory}\n")

for article in newsArticles:
    print("=" * 80)
    print(f"📰  {article['title']}\n")
    print(f"By: {article['author']} | 🕒 Published At: {article['publishedAt']} | 🌐 Source: {article['source']['name']}\n")
    print(f"📄 Description:\n{article['description']}\n")
    print(f"🧾 Content Preview:\n{article['content']}\n")
    print(f"🔗 Read more: {article['url']}")
    print("=" * 100 + "\n")