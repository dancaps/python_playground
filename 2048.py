"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    results = []
    mem = 0
    count = 0
    for i in line:
        if i == 0 and mem != 0:
            results.append(mem)
            mem = 0
            count += 1
        elif i == 0 and mem == 0:
            count += 1
        elif i != 0 and mem == 0:
            mem = i
        elif i == mem:
            results.append(i + mem)
            mem = 0
            count += 1
        elif i != 0 and i != mem:
            results.append(mem)
            mem = i
        else:
            results.append(mem)
            count += 1

    while count > 0:
        results.append(0)
        count -= 1

    return results

print merge([2, 0, 2, 4])
print merge([0, 0, 2, 2])
print merge([2, 2, 0, 0])
print merge([2, 2, 2, 2, 2])
print merge([8, 16, 16, 8])