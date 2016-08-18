#!/usr/bin/env python3

def is_even(n):
    """Function to test if a number (n) is an even or odd number

    Args:
        n (int)

    Returns:
        bool: Returns True if the number is even or False if it's odd.

    """

    if n%2 == 0:
        return True
    else:
        return False

def is_prime(n):
    """Function to test if a number (n) is a prime number

    Args:
        n (int)

    Returns:
        bool: Returns True if the number is prime or False if it's not.

    """

    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#main
while True:
    #user selection
    print("Enter the number of the program you would like to run.")
    print("1 - Check whether a number is even or odd")
    print("2 - Check if a number is a prime number")
    selection = int(input("Make selection:\n"))

    #this code uses the is_even function to tell the user if the number is even or odd
    if selection == 1:
        n = int(input("Enter your number to see if it's even or odd:"))
        if is_even(n) == True:
            print(str(n) + " is an even number\n")
        else:
            print(str(n) + " is an odd number\n")

    #this code uses the is_prime function to tell the user if the number is a prime number
    elif selection == 2:
        n = int(input("Enter your number to see if it's a prime number:"))
        if is_prime(n) == True:
            print(str(n) + " is a prime number\n")
        else:
            print(str(n) + " is not a prime number\n")

    #this code catches all invalid entries by the user and starts the program again
    else:
        print("You've entered an incorrect selection. Please try again.\n")