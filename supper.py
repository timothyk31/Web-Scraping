import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://engineering.tamu.edu/cse/profiles/index.html#Faculty').text
soup = BeautifulSoup(html_text, 'lxml')
desc = soup.find_all('div', class_ = 'profile')
results = ''
