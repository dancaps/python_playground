#!/usr/bin/env python3

'''https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

Simple Pig Latin

Move the first letter of each word to the end of it, then add 'ay' to the end of the word.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
'''

def pig_it(text):
    text = text.split(' ')
    answer = []

    for word in text:
        if '!' in word:
            if len(word) == 1:
                answer.append(word)
                continue
            for c in word:
                new_word = ''
                if c == '!':
                    continue
                new_word += c
            answer.append(new_word[1:] + new_word[:1] + 'ay!')
        if '?' in word:
            if len(word) == 1:
                answer.append(word)
                continue
            for c in word:
                new_word = ''
                if c == '?':
                    continue
                new_word += c
            answer.append(new_word[1:] + new_word[:1] + 'ay?')
        else:
            answer.append(word[1:] + word[:1] + 'ay')
    return ' '.join(answer)


print(pig_it('Oay emporatay oay oresmay !'))# uisQay ustodietcay psosiay ustodescay ?)
print(pig_it('This! is my string'))#,'hisTay siay ymay tringsay')