n = 100
numbers = [x for x in range(2,n,2)]

results =[]
new_num = list(numbers)

while len(numbers) > 0: # tests that numbers still has numbers
    results.append(numbers[0])
    print('Results',results)
    for index in range(len(numbers)): # pulls the index number for the copy of number list
        print('index', index)
        print('new_num value', numbers[index])
        if results[-1] % numbers[index] == 0:
            print('value of last item in results', results[-1])
            print('new_num value', numbers[index])
            numbers.remove(numbers[index])
    break    
print(len(results))



'''
For the life of me I can not figure out why n = 100 makes len(results) = 25.

I can only think that I must not understand the question
1. Initialize n to be 1000. Initialize numbers to be a list of numbers from 2 to n, but not including n.
        n = 100
        numbers = range(1, n, 2)
2. With results starting as the empty list, repeat the following as long as numbers contains any numbers.
        results = []
        while len(numbers) > 0:
Add the first number in numbers to the end of results.
            results.append(numbers[0])
Remove every number in numbers that is evenly divisible by (has no remainder when divided by) the number that you had just added to results.
            for index in range(len(numbers)):
                if results
'''
