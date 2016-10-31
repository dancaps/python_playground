def square_digits(num):
    num = str(num)
    answer = ''
    sq = str()
    
    for d in num:
        d = int(d)
        sq = d * d
        answer += str(sq)
    return(int(answer))

print(square_digits(9119))
