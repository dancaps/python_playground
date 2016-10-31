nums = '''
432 124 365 101 409 155 209 186 421 573 189 446 579 55 492 67 408 499 218 580 221 32 401 300 347 545 357 337 69 425 527 470 517
'''

nums = nums.split()

def f2c(fahren):
    fahren = int(fahren)
    cel = (fahren - 32) * 5 / 9
    if cel == 0:
        print(0)
        return
    remainder = cel % int(cel)
    if remainder == 0:
        print(int(cel))
    elif remainder >= .5:
        print(int(cel) + 1)
    else:
        print(int(cel))

for i in nums:
    i = int(i)
    f2c(i)

