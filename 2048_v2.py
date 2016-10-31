"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    results = [0] * len(line)
    results_index = 0
    for item in line:
        if item > 0:
            results[results_index] = item
            results_index += 1
    for index in range(len(results)):
        try:
            if results[index] == results[index + 1]:
                results[index] *= 2
                results.pop(index + 1)
                results.append(0)
        except IndexError:
            continue
    return results

print merge([2, 0, 2, 4])
print merge([0, 0, 2, 2])
print merge([2, 2, 0, 0])
print merge([2, 2, 2, 2, 2])
print merge([8, 16, 16, 8])