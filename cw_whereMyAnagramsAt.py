#!/usr/bin/env python3

'''https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

'''
def anagrams(word, words):
    key_word = list(word.lower())
    words = [x.lower() for x in words]
    answer = []
    #print(key_word, words, answer)
    for element in words:
        if len(element) != len(key_word):
            continue
        w = list(element)
        for c in key_word:
            if c in w:
                w.remove(c)
        if len(w) == 0:
            answer.append(element)
    return answer





print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))# ['aabb', 'bbaa']
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))#, ['carer', 'racer']))