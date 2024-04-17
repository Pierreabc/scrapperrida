import requests
from bs4 import BeautifulSoup


URL = 'https://www.scrapethissite.com/pages/simple/'
s = requests.Session()
r = s.get(URL)



soup = BeautifulSoup(r.text, 'html.parser')

capital_tags = soup.find_all('span', class_='country-capital')

for tag in capital_tags:
    print(tag.text)