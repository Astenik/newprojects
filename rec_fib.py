def rec_fib(n):
     '''this function returns fibonachi's n-td number in a recursiv way.'''
     if n == 1 or n == 2:
           return 1 
     return rec_fib(n - 1) + rec_fib(n - 2)

n = int(input("insert the n: "))
print(f"the {n}-td number of fibonachi is eual to: {rec_fib(n)}")
