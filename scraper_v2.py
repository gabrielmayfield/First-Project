# Import the required libraries
import sys
import requests
from bs4 import BeautifulSoup

# Print the Python version to confirm the version being used
print(sys.version)

# Make a request to the Wikipedia Main Page.
# This sends a GET request to the specified URL and saves the response from server in our variable 'r'.
r = requests.get("https://en.wikipedia.org/wiki/Main_Page")

# 'r.content' contains the raw HTML content of the page.

# Create a BeautifulSoup object and specify the parser library at the same time.
# BeautifulSoup object transforms a complex HTML document into a tree of Python objects.
soup = BeautifulSoup(r.content, 'html.parser')

# Extract the title of the page by finding the 'title' tag. 
# 'find' method returns the first matching tag (and its contents).
page_title = soup.find('title')
# Print the text part of the page title
print(f"Page Title: {page_title.text}")  

# Extract the main heading of the page by finding the 'h1' tag.
main_heading = soup.find('h1')
# Print the text part of the main heading
print(f"Main Heading: {main_heading.text}")

# Extract 'In the news' section by finding the div with id 'mp-itn'
# 'find' method can also search for tags with specific attributes, in this case, an id.
in_the_news_section = soup.find('div', id='mp-itn')

# Extract all the news items in 'In the news' section
# 'find_all' returns a list of all matching tags and their contents.
news_items = in_the_news_section.find_all('li')

# Print each news item
print("\nIn the News:")
for item in news_items:
    # Print the text part of each news item
    print(item.text)
