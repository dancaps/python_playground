###Version 1

print('Tell me a number')
inputNumber = input()
x = True
  
def collatz(number):
    if number % 2 == 0:
        print(str(number // 2))
    else:
        newNumber = number * 3 + 1
        print(str(newNumber))

while x == True:
    try:
        functionNumber = int(inputNumber)
        collatz(functionNumber)
        x = False
    except:
        print('This is not a number. Please try again.')
        break

#version 2
    
print('Tell me a number')
inputNumber = input()
  
def collatz(number):
    if number % 2 == 0:
        print(str(number // 2))
    else:
        newNumber = number * 3 + 1
        print(str(newNumber))

try:
    functionNumber = int(inputNumber)
    collatz(functionNumber)
except:
    print('This is not a number. Please try again.')
