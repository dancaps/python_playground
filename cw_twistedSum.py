#!/usr/bin/env pthon3

'''https://www.codewars.com/kata/twisted-sum/train/python
Twisted Sum
Find the sum of the digits of all the numbers from 1 to N (both ends included).

For N = 10 the sum is 1+2+3+4+5+6+7+8+9+(1+0) = 46

For N = 11 the sum is 1+2+3+4+5+6+7+8+9+(1+0)+(1+1) = 48

For N = 12 the sum is 1+2+3+4+5+6+7+8+9+(1+0)+(1+1) +(1+2)= 51
'''
def compute_sum(n):
    l = [str(i) for i in range(n + 1)]
    answer = 0
    for n in l:
        for i in n:
            answer += int(i)
    return answer


print(compute_sum(10))
#
# cases = ((1, 1), (2, 3), (3, 6), (4, 10), (10, 46))
# for inp, res in cases:
#     test.assert_equals(compute_sum(inp), res)