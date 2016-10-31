def factorial(n):
    answer = 1
    if n < 0:
        return None
        
    while n > 0:
        answer = answer * n
        n -= 1
    
    return answer

print(factorial(-5))
    
    
