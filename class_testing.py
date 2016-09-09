#!/usr/bin/env python3

from Beatles_Class import Beatles

Beatles().the_walrus()
b = Beatles()
b.the_walrus()

t = Beatles()
print(b.i_am)

b.i_am = "Danny"
print(b.i_am)
print(t.i_am)

