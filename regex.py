import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "regex_sum_42.txt"
handle = open(name)

numbers = []
sum_numbers = 0

for line in handle:
    lst = re.findall('[0-9]+', line)
    if len(lst) > 0:
        numbers += lst

for i in numbers:
    sum_numbers += int(i)

print sum_numbers