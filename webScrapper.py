import sys
import requests
from pathlib import Path
from bs4 import BeautifulSoup
r = requests.get('https://holybooks.com/the-complete-works-of-friedrich-nietzsche-in-english-as-pdf/')
# print(r.text)
print(sys.path[0])
soup = BeautifulSoup(r.text, 'html.parser')
for a in soup.find_all('a', href=True):
    # print("Found the URL:", a['href'])
    arr = a['href'].split('.')
    if arr[-1] == 'pdf':
        response = requests.get('http:'+a['href'])
        # print(response.content)
        with open(Path(sys.path[0], a.string+'.pdf'), 'wb+') as f:
            f.write(response.content)
