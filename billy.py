import urllib
import xml.etree.ElementTree as ET
total = 0

url = 'http://python-data.dr-chuck.net/comments_199849.xml '
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)

counts = tree.findall('.//count')
print len(counts)

for items in counts:
    total += int(items.text)

print total
