from bs4 import BeautifulSoup
import requests

# # HTML From File
# with open("index.html", "r") as f:
# 	doc = BeautifulSoup(f, "html.parser")


# tags = doc.find_all("p")[0]

# print(tags.find_all("b"))

# HTML From Website
url = "https://www.vogelwarte.ch/en/birds/birds-of-switzerland/black-woodpecker"
# https://www.vogelwarte.ch/en/birds/birds-of-switzerland/black-woodpecker
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print(doc)

prices = doc.find_all(string="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)
