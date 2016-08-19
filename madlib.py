#!/usr/bin/env python3
# week 2 assignment 2 :: madlibs


sample_dict = {"verb1" : "BANISH", "noun1" : "PENCIL", "adjective1" : "INSTITUTIONAL",
               "gov_pos1" : "COURT CLERK", "holiday1" : "HALLOWEEN", "occupation1" : "FLIGHT ATTENDANTS",
               "verb2" : "TURN", "crime1" : "SPEED", "verb3" : "COMMUNE", "adjective2" : "MASSIVE",
               "noun2" : "TAX", "noun3": "LASER GUN"}
sample_text = "1. You shall not {verb1} any other {noun1}.\n" \
              "2. You shall not make a {adjective1} image.\n" \
              "3. You shall not take the name of the {gov_pos1} in vain.\n" \
              "4. You shall not break the {holiday1}.\n" \
              "5. You shall not dishonor your {occupation1}.\n" \
              "6. You shall not {verb2}.\n" \
              "7. You shall not commit {crime1}.\n" \
              "8. You shall not {verb3}.\n" \
              "9. You shall not bear {adjective2} witness against thy {noun2}.\n" \
              "10. You shall not covet thy neighbor`s {noun3}.\n"
# print(sample_dict)
# print(sample_text).format(verb1 = sample_dict["verb1"], noun1 = sample_dict["noun1"],
#                   adjective1 = sample_dict["adjective1"], gov_pos = sample_dict["gov_pos"],
#                   holiday = sample_dict["holiday"], occupation = sample_dict["occupation"],
#                   verb2 = sample_dict["verb2"], crime = sample_dict["crime"], verb3 = sample_dict["verb3"],
#                   adjective2 = sample_dict["adjective2"], noun2 = sample_dict["noun2"],
#                   noun3 = sample_dict["noun3"])

while True:
    sample_run = input("Would you like to see the sample madlib? y for YES or n for NO or q to QUIT\n")

    if sample_run == "y":
        print("These are the sample words:\n")
        for key, value in sample_dict.items():
            print(key[:-1], value)
        print("")
        print("#" * 75, "\n")
        print(sample_text.format(verb1 = sample_dict["verb1"], noun1 = sample_dict["noun1"],
                                  adjective1 = sample_dict["adjective1"], gov_pos1 = sample_dict["gov_pos1"],
                                  holiday1 = sample_dict["holiday1"], occupation1 = sample_dict["occupation1"],
                                  verb2 = sample_dict["verb2"], crime1 = sample_dict["crime1"],
                                  verb3 = sample_dict["verb3"], adjective2 = sample_dict["adjective2"],
                                  noun2 = sample_dict["noun2"], noun3 = sample_dict["noun3"]))
    elif sample_run == "n":
        pass
    elif sample_run == "q":
        print("Thank you for playing! THE END!")
        break
    else:
        print("You made an incorrect selection. Please try again")
        continue