#!/usr/bin/env python3

'''http://www.codewars.com/kata/rotate-for-a-max/train/python
Take a number: 56789. Rotate left, you get 67895.

Keep the first digit in place and rotate left the other digits: 68957.

Keep the first two digits in place and rotate the other ones: 68579.

Keep the first three digits and rotate left the rest: 68597. Now it is over since keeping the first four it remains
only one digit which rotated is itself.

You have the following sequence of numbers:

56789 -> 67895 -> 68957 -> 68579 -> 68597

and you must return the greatest: 68957.

Calling this function max_rot (or maxRot or ... depending on the language)

max_rot(56789) should return 68957
'''
def max_rot(n):
    n = list(str(n))
    print(n)
    answer = [''.join(n)]
    print(answer)
    for i in range(len(n)):
        n = n[i + 1:] + n[:i + 1]
        print(n)
        # if new_string > answer[0]:
        #     answer[0] = new_string
    print(answer)


print(max_rot(56789))#, 85821534)
'''
def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe("max_rot")
Test.it("Basic tests")
testing(max_rot(38458215), 85821534)
testing(max_rot(195881031), 988103115)
testing(max_rot(896219342), 962193428)
testing(max_rot(69418307), 94183076)
'''