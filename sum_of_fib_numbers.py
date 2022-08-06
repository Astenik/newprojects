def if_fib(number:int):
      ''' this function checks if the number given as an argument 
      is a member of fibonachi.'''
      num1 = 1
      num2 = 1 
      res = num1 + num2
      while res < number:
           num1 = num2
           num2 = res
           res = num1 + num2
      if res == number:
           return True
      else:
           return False
def sum_of_fib_numbers(length_of_interval:float): 
      '''this function counts sum of fibonachi members in given 
      interval that are also even numbers.'''
      sum = 0
      for num in range(length_of_interval):
            if if_fib(num) and (num % 2 == 0):
                  sum += num 
      return sum 

print(sum_of_fib_numbers(50))
