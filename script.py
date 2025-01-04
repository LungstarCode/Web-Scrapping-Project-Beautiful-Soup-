import requests

# getting data from HTML document
URL = 'https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/'
r = requests.get(URL)

print(r.content)
