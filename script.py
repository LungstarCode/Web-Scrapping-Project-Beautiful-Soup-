
# step 1: imports
import requests
from bs4 import BeautifulSoup

# step 2: Extract HTML
# getting data from HTML document
URL = 'https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/'
r = requests.get(URL)

# Step 3: Parsing the HTML conent 

soup = BeautifulSoup(r.content , 'html5lib')  # creates a bs object and specify the parser 
print(soup.prettify())  # prints the html content



