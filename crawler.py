from bs4 import BeautifulSoup
import urllib

url = raw_input('Enter the url:')

if len(url) < 1:
    url = "http://dancaps.com/"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup.find_all('a')

for t in tags:
    print t.get('href', None)