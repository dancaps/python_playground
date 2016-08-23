#!/usr/bin/env python3

'''http://www.codewars.com/kata/546937989c0b6ab3c5000183/train/python

Caesar Ciphers are one of the most basic forms of encryption. It consists of a message and a key, and it shifts the
letters of the message for the value of the key.

Your task is to create a function encryptor that takes 2 arguments - key and message - and returns the encrypted message.

A message 'Caesar Cipher' and a key of 1 returns 'Dbftbs Djqifs'.

A message 'Caesar Cipher' and a key of -1 returns 'Bzdrzq Bhogdq'.

Make sure to only shift letters, and be sure to keep the cases of the letters the same. All punctuation, numbers,
spaces, and so on should remain the same.

Also be aware of keys greater than 26 and less than -26. There's only 26 letters in the alphabet!

'''

def encryptor(key, message):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encrypted_message = ''
    new_character = ''

    #if key < -26 or key > 26:
    #   raise Exception("Invalid Key!")

    for character in message:
        upper_case = False
        if character.lower() not in alphabet:
            encrypted_message += character
            continue

        if character.isupper() == True:
            upper_case = True

        character_index = alphabet.index(character.lower())

        count = 0
        if key > 0:
            while count <= key:
                new_character = alphabet[(character_index + count) % len(alphabet)]
                count += 1
        else:
            while count <= (key * -1):
                new_character = alphabet[(character_index - count) % len(alphabet)]
                count += 1

        if upper_case == True:
            encrypted_message += new_character.upper()
        else:
            encrypted_message += new_character

    print(message)
    print(encrypted_message)
    return encrypted_message


encryptor(-5, 'Hello World!')
