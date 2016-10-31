nums = '''
2634848 19
-4040002 147482
11495 956
7369 1108
6532986 926
6701 434
7567 700
5738140 647
3398091 -2703989
1040056 861908
7260419 768
3222743 66
-9011693 341897
4141 1592
-3655613 -1405372
'''

nums = nums.split()
dividend = nums[::2]
divisor = nums[1::2]
quotient = 0.0

for a, b in zip(dividend, divisor):
    global quotient
    a = int(a)
    b = int(b)
    quotient = a / b
    remainder = quotient % int(quotient)
    if remainder == 0:
        print(int(quotient))
    elif remainder >= .5:
        print(int(quotient) + 1)
    else:
        print(int(quotient))
        

