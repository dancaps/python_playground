import math

p = [4, 7]
q = [1, 9]
r = 2

def distance(p, q):
    print(p, q)
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

print(distance(p, q))
