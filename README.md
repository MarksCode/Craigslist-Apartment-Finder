# Craigslist Apartment Finder

Find apartments in your area!

## Description

Simple script that scrapes craigslist to find listings under a given price in a given zipcode

### Executing program

```
usage: python3 apartmentFinder.py [-h] [--open] zip [price] [distance]

positional arguments:
  zip         zip code to search
  price       max price to find (default=10,000)
  distance    max distance to search (default=0)

optional arguments:
  -h, --help  show this help message and exit
  --open      experimental: open found listings in chrome
```
