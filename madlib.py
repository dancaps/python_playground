#!/usr/bin/env python3
#week 2 assignment 2 :: madlibs

#this is the dict used if the user selects to use the built in sample
sample_dict = {"verb1" : "BANISH",
               "noun1" : "PENCIL",
               "adjective1" : "INSTITUTIONAL",
               "government_position1" : "COURT CLERK",
               "holiday1" : "HALLOWEEN",
               "occupation1" : "FLIGHT ATTENDANTS",
               "verb2" : "TURN",
               "crime1" : "SPEED",
               "verb3" : "COMMUNE",
               "adjective2" : "MASSIVE",
               "noun2" : "TAX",
               "noun3": "LASER GUN"}

def make_madlib(madlib_dict):
    """this function takes a properly formatted dictionary as input and prints the madlib

    Args:
        madlib_dict (dict): it must contain the following keys
            verb1
            verb2
            verb3
            noun1
            noun2
            noun3
            adjective1
            adjective2
            occupation1
            crime1
            government_position1
            holiday1

    Returns:
        print: it prints the madlib containing the data from the dictionary

    """
    madlib = "1. You shall not {verb1} any other {noun1}.\n" \
             "2. You shall not make a {adjective1} image.\n" \
             "3. You shall not take the name of the {government_position1} in vain.\n" \
             "4. You shall not break the {holiday1}.\n" \
             "5. You shall not dishonor your {occupation1}.\n" \
             "6. You shall not {verb2}.\n" \
             "7. You shall not commit {crime1}.\n" \
             "8. You shall not {verb3}.\n" \
             "9. You shall not bear {adjective2} witness against thy {noun2}.\n" \
             "10. You shall not covet thy neighbor`s {noun3}.\n"

    print("These are the words you've selected:\n")
    for key, value in madlib_dict.items():  #prints the dict in human readable format so the user can see the data
        print(key[:-1], value)
    print("")
    print("#" * 75, "\n")  #created a line to seperate the text
    print(madlib.format(verb1=madlib_dict["verb1"],
                        noun1=madlib_dict["noun1"],
                        adjective1=madlib_dict["adjective1"],
                        government_position1=madlib_dict["government_position1"],
                        holiday1=madlib_dict["holiday1"],
                        occupation1=madlib_dict["occupation1"],
                        verb2=madlib_dict["verb2"],
                        crime1=madlib_dict["crime1"],
                        verb3=madlib_dict["verb3"],
                        adjective2=madlib_dict["adjective2"],
                        noun2=madlib_dict["noun2"],
                        noun3=madlib_dict["noun3"]))

#main
while True:
    #prompts the user to find out if they want to use the provided sample or add their own words
    sample_run = input("Would you like to see the sample madlib or add your own words?\n"
                       "y to use the sample madlib\n"
                       "n to add your own words\n"
                       "q to QUIT\n")

    if sample_run == "y":  #if the user selects yes this code will run
        make_madlib(sample_dict) #calls the function with the properly formatted dict

    elif sample_run == "n":  #if the user selects no this code will run
        a_an = ''  #allows for proper grammar when prompting the user
        vowel = ["a", "e", "i", "o", "u"]  #used to see if there the word starts with a vowel
        user_dict = {}  #empty dict that will be populated by user input
        user_list = list(sample_dict)  #this creates a list of the keys from the sample dict
        print("You will be prompted to enter the required words")
        for i in user_list:  #this iterates though the new list and uses the element names to populate the new dict
            if i[0] in vowel:  #checks to see if the first letter is a vowel and chooses a or an based on that info
                a_an = 'an'
            else:
                a_an = 'a'
            user_dict[i] = input("Enter " + a_an +" " + i[:-1] + "\n")  #prompts the users with the type of info to enter
        make_madlib(user_dict)  #calls the function with the properly formatted dict

    elif sample_run == "q":  #quits the madlib
        print("Thank you for playing! THE END!")
        break

    else:  #catches incorrect user entries and restarts the program
        print("You made an incorrect selection. Please try again")
        continue