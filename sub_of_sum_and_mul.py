def sub_of_sum_and_mul(num):
      '''this function returns the  subtraction of sum and mul of num's digits.'''
      _sum = 0
      _mul = 1
      while not num == 0:
           _sum += num % 10 
           _mul *= num % 10
           num = num // 10
      return (_mul - _sum)
number = int(input("insert the number: "))
print(f" the subtraction of my {number}'s digits's mul and sum is equal to: {sub_of_sum_and_mul(number)}")
