import requests
from bs4 import BeautifulSoup
import pandas as pd

# Simple Jumia scraper example
url = "https://www.jumia.co.ke/smartphones/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

products = []
for item in soup.select("article.prd"):
    name = item.select_one("h3.name")
    price = item.select_one("div.prc")
    if name and price:
        products.append({"name": name.text, "price": price.text})

df = pd.DataFrame(products)
df.to_csv("data.csv", index=False)
print(f"Saved {len(products)} products")
