import requests
from bs4 import BeautifulSoup


def crawl_ecommerce(url):
    try:
        # Step 1: Establish HTTP connection and fetch page content
        response = requests.get(url)
        response.raise_for_status()  # Check for errors

        # Step 2: Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Step 3: Extract product data
        products = soup.find_all('article', class_='product_pod')
        print(f"\nCrawled {len(products)} products from: {url}\n")

        for product in products:
            title = product.h3.a['title']
            link = product.h3.a['href']
            price = product.find('p', class_='price_color').text

            # Step 4: Display product information
            print(f"Product: {title}")
            print(f"Price: {price}")
            print(f"Link: https://books.toscrape.com/catalogue/{link}")
            print("-" * 50)

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")


if __name__ == "__main__":
    site = "https://books.toscrape.com/"
    crawl_ecommerce(site)
