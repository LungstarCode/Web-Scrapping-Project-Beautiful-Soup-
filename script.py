
# step 1: imports
import requests
from bs4 import BeautifulSoup

# step 2: Extract HTML
# getting data from HTML document
URL = 'http://quotes.toscrape.com/'
r = requests.get(URL)

# Step 3: Parsing the HTML conent 

soup = BeautifulSoup(r.content , 'html5lib')  # creates a bs object and specify the parser 
#print(soup.prettify())  # prints the html content

# Step 4: selecting wat we want to extract 

# Extracting quotes, authors, and tags
quotes = soup.find_all('div', class_='quote')

# Looping through each quote and extracting the details
for quote in quotes:
    # Quote text
    text = quote.find('span', class_='text').get_text()
    
    # Author name
    author = quote.find('small', class_='author').get_text()
    
    # Tags associated with the quote
    tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
    
    # Print the details
    print(f"Quote: {text}")
    print(f"Author: {author}")
    print(f"Tags: {', '.join(tags)}")
    print("-" * 80)