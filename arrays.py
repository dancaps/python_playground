def up_array(arr):
    answer = ''
    new_list = []
    if arr == []:
        return None
    for i in arr:
        if i > 0 and i <= 10:
            answer += str(i)
        else:
            return None
    answer = int(answer) + 1
    for ch in str(answer):
        new_list.append(int(ch))
    return new_list


print(up_array([1, 11]))

#Test.assert_equals(up_array([2,3,9]), [2,4,0])
#Test.assert_equals(up_array([4,3,2,5]), [4,3,2,6])
#Test.assert_equals(up_array([1,-9]), None)
