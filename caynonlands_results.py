from bs4 import BeautifulSoup
import urllib

url = "http://dancaps.com/files/rj.txt"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

print soup.get_text()

