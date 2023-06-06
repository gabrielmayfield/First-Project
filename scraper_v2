import sys
import requests
from bs4 import BeautifulSoup

print(sys.version)

# Make a request to the website
r = requests.get("https://en.wikipedia.org/wiki/Main_Page")
r.content

# Use the 'html.parser' to parse the page
soup = BeautifulSoup(r.content, 'html.parser')

# Extract title of the page
page_title = soup.find('title')
print(f"Page Title: {page_title.text}")  # .text will return the text between the tags

# Extract main heading of the page
main_heading = soup.find('h1')
print(f"Main Heading: {main_heading.text}")

# Extract 'In the news' section
in_the_news_section = soup.find('div', id='mp-itn')

# Extract all the items in 'In the news' section
news_items = in_the_news_section.find_all('li')

print("\nIn the News:")
for item in news_items:
    print(item.text)
