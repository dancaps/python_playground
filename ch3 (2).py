def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return int(number // 2)
    if number % 2 == 1:
        print(3 * number + 1)
        return int(3 * number + 1)


raw_int =   input("Enter a integer:")

try:
    number = int(raw_int)
    while number != 1:
        number = collatz(number)
except:
    print("You did not enter a number")

