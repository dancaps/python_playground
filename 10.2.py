name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = {}

for line in handle:
    if line.startswith('From '):
        hour_pos = line.find(':')
        hour = line[hour_pos - 2: hour_pos]
        count[hour] = count.get(hour, 0) + 1

for k, v in sorted(count.items()):
    print k, v

