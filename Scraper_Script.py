import requests
import pandas as pd
from bs4 import BeautifulSoup
##

urls = ['https://usa.banggood.com/Wholesale-Computers-and-Office-c-155.html',
        'https://usa.banggood.com/Wholesale-Consumer-Electronics-c-11123.html?direct=13']
product_name = []
product_price = []
product_review = []
search = []

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find('div', class_="product-list")
    if results is None:
        print('No results')
        continue
    products = results.find_all('div', class_='p-wrap')
    for product in products:
        title = product.find('a', class_='title')
        price = product.find('span', class_='price-box')
        review = product.find('a', class_='review')
        product_name.append(title.text.strip())
        product_price.append(price.text.strip())
        product_review.append(review.text.strip())
        search.append(url)



##

table = {"Product Name":product_name, "Price":product_price, "Reviews":product_review, "URL":search}
df = pd.DataFrame(table, columns=['Product Name',
                                  'Price',
                                  'Reviews',
                                  'URL'])
df.to_csv("Product_Scrape.csv", index=False, header=True, encoding="utf-8")
print('Exported.')

    
