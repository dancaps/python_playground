
def make_madlib(text, word_dict):
    pass



sample_dict = {"verb1" : "BANISH", "noun1" : "PENCIL", "adjective1" : "INSTITUTIONAL", \
               "gov_pos" : "COURT CLERK", "holiday" : "HALLOWEEN", "occupation" : "FLIGHT ATTENDANTS",
               "verb2" : "TURN", "crime" : "SPEED", "verb3" : "COMMUNE", "adjective2" : "MASSIVE",
               "noun2" : "TAX", "noun3": "LASER GUN"}
sample_text = "1. You shall not {verb1} any other {noun1}.\n" \
              "2. You shall not make a {adjective1} image.\n" \
              "3. You shall not take the name of the {gov_pos} in vain.\n" \
              "4. You shall not break the {holiday}.\n" \
              "5. You shall not dishonor your {occupation}.\n" \
              "6. You shall not {verb2}.\n" \
              "7. You shall not commit {crime}.\n" \
              "8. You shall not {verb3}.\n" \
              "9. You shall not bear {adjective2} witness against thy {noun2}.\n" \
              "10. You shall not covet thy neighbor`s {noun3}.\n"
print(sample_dict)
#print("help")
'''print(sample_text).format(verb1 = sample_dict["verb1"], noun1 = sample_dict["noun1"],
                          adjective1 = sample_dict["adjective1"], gov_pos = sample_dict["gov_pos"],
                          holiday = sample_dict["holiday"], occupation = sample_dict["occupation"],
                          verb2 = sample_dict["verb2"], crime = sample_dict["crime"], verb3 = sample_dict["verb3"],
                          adjective = sample_dict["adjective2"], noun2 = sample_dict["noun2"],
                          noun3 = sample_dict["noun3"])

default_madlib = "This is my madlib"
#directions
print("You can write your own text for you madlib\nto insert you")

user_madlib = input("Enter the text using the format outlined above")


'''