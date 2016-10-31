from bs4 import BeautifulSoup
import urllib

url = raw_input('Enter the url:')
count = int(raw_input('Count:'))
pos = int(raw_input('Enter position:'))

if len(url) < 1:
    url = "http://python-data.dr-chuck.net/known_by_Edie.html"

while count + 1 > 0:
    print 'Retrieving:', url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    a = soup.find_all('a')
    url = a[int(pos) - 1].get('href')
    count -= 1

