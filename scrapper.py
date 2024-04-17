import requests
from bs4 import BeautifulSoup


URL = 'https://www.scrapethissite.com/pages/simple/'
s = requests.Session()
r = s.get(URL)



soup = BeautifulSoup(r.text, 'html.parser')

country_tags = soup.find_all('h3')

for tag in country_tags:
    print(tag.text)