import json
import urllib
characters = 0
count = 0
total = 0

url = raw_input('Enter the url:')
if len(url) < 1:
    url = "http://python-data.dr-chuck.net/comments_199853.json"
print 'Retrieving ' + url
input = urllib.urlopen(url).read()
info = json.loads(input)

for item in info['comments']:
    count += 1
    total += item['count']

#print 'Retrieved', characters, 'characters'
print 'Count:', count
print 'Sum:', total
