import requests 
from bs4 import BeautifulSoup

response = requests.get('https://github.com/trending/python?since=daily')

soup = BeautifulSoup(response.text, 'html.parser')

repo_list = soup.find_all('h1', {'class': 'h3 lh-condensed'})

for repo in repo_list:
    print(repo.text.strip())
