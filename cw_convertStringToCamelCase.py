#!/usr/bin/env python3
'''https://www.codewars.com/kata/convert-string-to-camel-case/train/python
Convert string to camel case

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.

Examples:

# returns "theStealthWarrior"
to_camel_case("the-stealth-warrior")

# returns "TheStealthWarrior"
to_camel_case("The_Stealth_Warrior")

'''
def to_camel_case(text):
    words = []
    if len(text) == 0:
        return ''
    if '-' in text:
        text = text.replace('-', '_')
    words = text.split('_')
    return ''.join([words.pop(0)] + [w.title() for w in words])

'''
test.describe("Testing function to_camel_case")
test.it("Basic tests")
test.assert_equals(to_camel_case(''), '', "An empty string was provided but not returned")
test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")
'''