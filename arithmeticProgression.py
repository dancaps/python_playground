nums = '''
2 6 68
23 15 69
5 10 48
21 7 46
30 9 75
29 1 42
25 19 68
29 1 90
10 7 65
'''

nums = nums.split()
a = nums[::3]
b = nums[1::3]
c = nums[2::3]

def arithmethic_progression(list1, list2, list3):
    for a, d, n in zip(list1, list2, list3):
        seq_num = int(a)
        step_up = int(d)
        iteration = int(n)
        answer = 0
        
        sum_list = []
        sum_list.append(seq_num)

        for tries in range(iteration - 1):
            seq_num += step_up
            sum_list.append(seq_num)
            
        for i in sum_list:
            answer += i 

        print(answer)
         
arithmethic_progression(a, b, c)
