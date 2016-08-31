#!/usr/bin/env python2

'''https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python
IP Validation

Instructions
Output
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. Input to the function is guaranteed
to be a single string.

Examples of valid inputs: 1.2.3.4 123.45.67.89

Examples of invalid inputs: 1.2.3 1.2.3.4.5 123.456.78.90 123.045.067.089
'''


def is_valid_IP(strng):
    octet_list = strng.split('.')  # string split the octets into 4 string list elements

    if len(octet_list) != 4 or False in [i.isalnum() == True for i in
                                         octet_list]:  # check that there are 4 octets and no letters
        return False

    for i in range(len(octet_list)):  # convert the elements to an int
        try:
            octet_list[i] = int(octet_list[i])
        except: # bad form I know but this was the only way codewars would work
            return False

    for i in range(len(octet_list)):
        if len(str(octet_list[i])) > 3:  # makes sure there are no more than 3 digits in the octet
            return False
        if octet_list[i] < 0 or octet_list[i] > 255: # makes sure the numbers are between 1 and 255
            return False
    if octet_list[0] == 123: # excluded any ip that starts with 123
        return False

    return True

print(is_valid_IP('12.255.56.1'))#,     True)
print(is_valid_IP(''))#,                False)
print(is_valid_IP('abc.def.ghi.jkl'))#, False)
print(is_valid_IP('123.456.789.0'))#,   False)
print(is_valid_IP('12.34.56'))#,        False)
print(is_valid_IP('12.34.56 .1'))#,     False)
print(is_valid_IP('12.34.56.-1'))#,     False)
print(is_valid_IP('123.045.067.089'))#, False)
