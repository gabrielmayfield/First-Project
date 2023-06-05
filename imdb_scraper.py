import requests
from bs4 import BeautifulSoup

# Make a request to the IMDb Top Rated Movies page
url = "https://www.imdb.com/chart/top/"
response = requests.get(url)
response.raise_for_status()

# Use the 'html.parser' to parse the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the movie list table
movie_table = soup.find('table', class_='chart')

# Find all the movie rows
movie_rows = movie_table.find_all('tr')

# Iterate over the movie rows and extract the movie details
for row in movie_rows[1:]:
    cells = row.find_all('td')
    rank = cells[0].text.strip()
    title = cells[1].a.text.strip()
    rating = cells[2].text.strip()
    year = cells[1].span.text.strip("()")
    
    print(f"Rank: {rank}")
    print(f"Title: {title}")
    print(f"Rating: {rating}")
    print(f"Year: {year}")
    print("---------------------")
