spam = ['apples', 'bananas', 'tofu', 'cats']

def sep(list):
    last_element = list[-1]
    list.pop(-1)
    return(', '.join(list) + ' and ' + str(last_element))

#print(sep(spam))

grid = [['.', '.', 'O', 'O', '.', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '.'],
        ['.', '.', 'O', 'O', 'O', 'O', 'O', '.', '.'],
        ['.', '.', '.', 'O', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', 'O', '.', '.', '.', '.']]

def print_grid(grid):
    for l in grid:
        print("".join(l))

print_grid(grid)