#!/usr/bin/env python3

'''http://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
Detect Pangram

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

'''

import string

def is_pangram(s):
    alpha = list(string.ascii_lowercase)
    s = list(s.lower())

    for i in s:
        if i in alpha:
            alpha.remove(i)

    if len(alpha) == 0:
        return True
    else:
        return False


pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram))#, True)
