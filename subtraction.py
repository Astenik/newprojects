def subtraction(num1, num2):
        '''this function counts the subtraction of 
        sum**2 and sum_mul. 'sum' is the sum of 
        all natural numbers in interval (num1, num2).
        sum_mul is the sum of quadros of all natural nubers 
        in interval (num1, num2).
        num1 is the firs argument of the function.
        num2 is the second argument of the function.'''
        sum = 0
        sum_mul = 0
        for num in range(num1, num2 + 1):
               sum_mul += num*num
               sum += num
        res = sum**2 - sum_mul
        return res

print(subtraction(1, 100))
