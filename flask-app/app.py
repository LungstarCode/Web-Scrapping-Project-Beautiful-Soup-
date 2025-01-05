from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_quotes():
    """Scrapes quotes, authors, and tags from the target website."""
    URL = 'http://quotes.toscrape.com/'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    quotes = soup.find_all('div', class_='quote')

    # Collect quotes data in a list of dictionaries
    data = []
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        data.append({
            'text': text,
            'author': author,
            'tags': tags
        })
    return data

@app.route('/')
def home():
    """Render the home page with the scraped quotes."""
    quotes_data = scrape_quotes()
    return render_template('home.html', quotes=quotes_data)

if __name__ == '__main__':
    app.run(debug=True)
