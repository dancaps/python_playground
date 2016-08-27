#!/usr/bin/env python3

from first_module import my_adder

for n in range(5):
    my_adder(n, 10)

for n in range(5):
    val = my_adder(n, 10, False)
    if val != n + 10:
        print('my_adder is broken')
        print('val should be {} but it is {}'.format(n + 10, val))
