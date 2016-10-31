print('How many cats do you have?')
numCats = input()

try:
    if int(numCats) < 0:
        print("You can't have negative cats!")
    elif int(numCats) < 1:
        print("You don't have any cats!")
    elif int(numCats) <= 3:
        print("You don't have very many cats at all.")
    elif int(numCats) > 3:
        print("You have way too many cats!")
except ValueError:
    print('You did not enter a number')
