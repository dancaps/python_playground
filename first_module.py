#!/usr/bin/env python3

def my_adder(a, b, verbose=True):
    if verbose:
    	print("I am running from inside my_adder")
    val = a + b
    if verbose:
        print("The value of a + b is: {}".format(val))
    return val
