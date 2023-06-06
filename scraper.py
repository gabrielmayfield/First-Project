import sys
print(sys.version)
import requests
from bs4 import BeautifulSoup

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

# Note: .text will return the text between the tags
