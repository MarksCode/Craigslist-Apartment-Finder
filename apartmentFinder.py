import requests
from bs4 import BeautifulSoup
import webbrowser
import argparse

parser = argparse.ArgumentParser('python3 apartmentFinder.py')
parser.add_argument('zip', help='zip code to search', type=int)
parser.add_argument('price', help='max price to find', nargs='?', type=int, default=10000)
parser.add_argument('distance', help='max distance to search', nargs='?', type=int, default=0)
parser.add_argument("--open", help="experimental: open found listings in chrome", action="store_true")
args = parser.parse_args()

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
url = 'https://sfbay.craigslist.org/search/pen/apa?sort=priceasc&availabilityMode=0&postal={0}&search_distance={1}'.format(args.zip, args.distance)
PRICE_MAX = args.price
found_listings = {}

source = requests.get(url).text
soup = BeautifulSoup(source, 'html.parser')
listings = soup.findAll('p', {'class': 'result-info'})
for listing in listings:
    priceElem = listing.find('span', {'class': 'result-price'})
    price = int(float(priceElem.text[1:]))
    if price <= PRICE_MAX:
        link = listing.find('a', {'class': 'result-title hdrlnk'})
        url = link['href']
        found_listings[url] = price

if len(found_listings) == 0:
    print('No listings with requirements found!')
else:
    for url, price in found_listings.items():
        if args.open:
            webbrowser.get(chrome_path).open(url)
        else:
            print('Listing found:\n   link: {0}\n   price: {1}'.format(url, price))
