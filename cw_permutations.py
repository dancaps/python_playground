#!/usr/bin/env python3

'''

https://www.codewars.com/kata/permutations/train/python
In this kata you have to create all permutations of an input string and remove duplicates, if present. This means,
you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
The order of the permutations doesn't matter.

'''
import itertools

def permutations(a):
    p = list(itertools.permutations(list(a)))
    p = set(p)
    answer = []

    for i in p:
        answer.append(''.join(list(i)))

    return answer

print(permutations('a'))

#assert_equals(sorted(permutations('a')), ['a'])
#assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
#assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
