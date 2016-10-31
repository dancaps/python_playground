import time

''' version 1
def russian_peasant(num1, num2):
    num1_list = []
    num2_list = []
    result = 0
    while int(num1) > 1:
        num1 = num1 / 2
        num1_list.append(int(num1))
        num2 = num2 * 2
        num2_list.append(int(num2))
    for x, y in zip(num1_list, num2_list):
        if x % 2 == 1:
            result += y
    return result
'''

# version 2
def russian_peasant(num1, num2):
    result = 0
    while int(num1) > 0:
        if num1 % 2 == 1:
            result += num2
        num1 = int(num1 / 2)
        num2 = int(num2 * 2)
    return result

def test_russian_peasant():
    assert russian_peasant(10, 10) == 100
    assert russian_peasant(357, 16) == 5712
    assert russian_peasant(5896, 96) == 566016
    assert russian_peasant(1234, 1234) == 1522756
    start_time = time.time()
    print(russian_peasant(1234000123456789012345678902345678900000, 121234567890976542345678903400000001231235546000))
    print(time.time() - start_time)

test_russian_peasant()

'''
357  X  16

X178     32
89      64
X44      128
X22      256
11      512
5       1024
X2       2048
1       4096
'''

