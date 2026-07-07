import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)
books = soup.find_all("article", class_="product_pod")

print(len(books))
data = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.find("p", class_="star-rating")["class"][1]
    availability = book.find("p", class_="instock availability").text.strip()

    data.append({
    "Title": title,
    "Price": price,
    "Rating": rating,
    "Availability": availability
})
    
    df = pd.DataFrame(data)

df.to_csv("books.csv", index=False)

print("Data saved successfully!")