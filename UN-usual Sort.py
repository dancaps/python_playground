# this function sorts strings, string numbers and integers into the following pattern. This would normally produce a "TypeError"
# order of elements in the returned array [string A-Z, string a-z, string numbers and integers mixed low to high, in the
# event you have both a string number and a integer of the same value the string number must come before the integer]

def unusual_sort(array):    
    # array with all the strings
    string = [s for s in array if type(s) == str]

    # array with only the ints
    integer = [s for s in array if type(s) == int]

    # array with all the string numbers
    snum = [s for s in string if s.isdigit()]

    # array for mutating the elements
    working_list = list(integer)


    #sorts the strings normally
    string.sort()

    # converts the string numbers to a ints and appends them to the working list 
    for s in snum:
        string.remove(s)
        working_list.append(int(s))

    # sorts the ints normally
    working_list.sort()

    # copies working_list
    return_list = list(working_list)

    # loops through the working_list, checks against the snum array and if there
    # is a match it converts it back to a string
    for i in working_list:
        print("2 DEBUG: type i = ", type(i))
        if str(i) in snum:
            snum.remove(str(i))
            return_list.reverse()
            return_list_index = return_list.index(i)
            return_list[return_list_index] = str(i)
            return_list.reverse()
            
    return string + return_list


array = [6, '7', 3, '7', 'H', '9', '9']
print(unusual_sort(array))
# results = ['a', 'a', 'f', 'z', 1, '1', 3, '3', 5, '5', '6', '22', 253]

'''
#This is what happens under normal circumstances. You aren't allowed to sort different types so it throws an error
>>> array = [1, 'a', '6', 'z', 'f', 3, 5, '1', '3', '5', 'a', 253, '22']
>>> array
[1, 'a', '6', 'z', 'f', 3, 5, '1', '3', '5', 'a', 253, '22']
>>> array.sort()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    array.sort()
TypeError: unorderable types: str() < int()



def unusual_sort(array):
    string = [s for s in array if type(s) == str]
    integer = [s for s in array if type(s) == int]
    string_num = [s for s in string if s.isdigit()]
    string_num_and_num = []
    string_num.sort()
    
    for s in string_num:
        string.remove(s)
        if int(s) in integer:
            a = int(s)
            string_num_and_num.append(a)
            string_num_and_num.append(s)
            integer.remove(a)
        else:
            string_num_and_num.append(s)
                                
    string.sort()
    integer.sort()
    print(string + string_num_and_num + integer)
'''



'''

def unusual_sort(array):
    string = [s for s in array if type(s) == str]
    integer = [s for s in array if type(s) == int]
    snum = [s for s in string if s.isdigit()]
    play_list = list(integer)
    string.sort()
    print("Created new integer list: ", play_list)

    for s in snum:
        string.remove(s)
        play_list.append(int(s))
    play_list.sort()
    print("This is the string number list: ", snum)
    print("Added the string numbers to the new list: ", play_list)

    for i in play_list:
        if str(i) in snum:
            print("These need to be changed to a string:", i)
            index = play_list.index(i)
            print("This is the index for the integer that needs to be turned into a string: ", index)
            play_list[index] = str(i)
            #play_list.insert(index, str(i))
            
    print(string + play_list)

unusual_sort( ['a', 'b', 'c', '1', '1', '2', '2', '2', '3', '3']) # should equal ['a', 'b', 'c', 1, '1', 2, '2', '2', 3, '3'])

unusual_sort(['0', '9', '8', '1', '7', '2', '6', '3', '5', '4'])#,["0","1","2","3","4","5","6","7","8","9"])
unusual_sort(['3', '2', '1', 'c', 'b', 'a'])#,["a","b","c","1","2","3"])
unusual_sort(['x', '1', 'y', '2', 'z', '3'])#,["x","y","z","1","2","3"])
unusual_sort(['c', 'b', 'a', '9', '5', '0', 'X', 'Y', 'Z'])#,["X","Y","Z","a","b","c","0","5","9"])
unusual_sort([3,"3","2",2,"2","1",1,"a","b","c"])#,["a","b","c",1,"1",2,"2","2",3,"3"],"should sort 'digits' after 'same-digit-numbers'")
unusual_sort(['0', '2', '4', 9, 1, 3, 5])# should equal ['a', 'b', 'c', '0', 1, '2', 3, '4', 5]
'''
