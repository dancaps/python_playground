#! /usr/bin/python2

fname = raw_input("Enter file name: ")
if fname == '':
    fname = 'romeo.txt'
fh = open(fname)
lst = list()
for line in fh:
    line = line.split()
    for i in line:
        if i in lst:
            continue
        lst.append(i)
lst2 = sorted(lst)
print lst2
