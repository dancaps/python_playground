#!/urs/bin/env python3

'''http://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
Maximum subarray sum
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
'''
import itertools

def maxSequence(arr):
    numbers = list(itertools.permutations(arr, 2))
    answer = [0]
    print(numbers)
    for n in numbers:
        if answer[0] < n[0] + n[1]:
            answer[0] = n[0] + n[1]
    return answer[0]

print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSequence([]))
'''
test.describe("Tests")
test.it('should work on an empty array')
test.assert_equals(maxSequence([]), 0)
test.it('should work on the example')
test.assert_equals(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
'''