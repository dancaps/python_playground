name = raw_input("Enter file:")
people = {}
offender = ()
count = 0

if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

for line in handle:
    if line.startswith('From:'):
        words = line.split()
        person = words[1]
        people[person] = people.get(person, 0) + 1

for a,b in people.items():
    if b > count:
        count = b
        offender = a,b

print offender[0], offender[1]
