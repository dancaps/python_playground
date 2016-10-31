from bs4 import BeautifulSoup
import urllib

url = raw_input('Enter the url:')

if len(url) < 1:
    url = "http://python-data.dr-chuck.net/comments_199852.html"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

span = soup.find_all('span')
total = 0

for i in span:
    total += int(i.string)

print "Count", len(span)
print "Sum", total