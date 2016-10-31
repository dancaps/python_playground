#! /usr/bin/python2

import os
#http://jessenoller.com/blog/2009/02/05/ssh-programming-with-paramiko-completely-different

#prompt user for the program and return the text to a string variable.
def get_program():
    file_name = ''
    while len(file_name) == 0:
        file_name = raw_input('Enter the full path to your program [\home\usr\sample.py]:')
        try:
            file_handler = open(file_name)
        except:
            print "ERROR :: That was an invalid entry. \nEither the file doesn't exist or the path is incorrect. Try again."
            file_name = ''
            continue
    return file_handler.read()

#create the temp directory with the program to stage it for sftp
def create_temp_program(program_string):
    basedir = '~/temp/'
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    #program = program_string.readlines()
    #print program

"""function to get the hosts via text file or individually. promtp the user to 
enter the host or location of a csv file
"""


"""function to make the connection"""

"""function to write the program"""

"""function to run the program"""


#program = get_program()
#print program

create_temp_program('Hello World!')