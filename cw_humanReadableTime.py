#!/usr/bin/env python3

'''https://www.codewars.com/kata/human-readable-time/train/python
Human Readable Time

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
'''

def make_readable(seconds):
    hours = seconds // 60 // 60
    minutes = seconds // 60 % 60
    seconds = seconds % 60
    if hours < 10:
        hours = '0' + str(hours)
    if minutes < 10:
        minutes = '0' + str(minutes)
    if seconds < 10:
        seconds = '0' + str(seconds)
    return str(hours) + ':' + str(minutes) + ':' + str(seconds)

print(make_readable(3601))


#Test.assert_equals(make_readable(0), "00:00:00")
#Test.assert_equals(make_readable(5), "00:00:05")
#Test.assert_equals(make_readable(60), "00:01:00")
#Test.assert_equals(make_readable(86399), "23:59:59")
#Test.assert_equals(make_readable(359999), "99:59:59")