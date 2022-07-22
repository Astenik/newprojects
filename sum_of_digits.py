def sum_of_digits(num):
      '''this function returns the count of digits of num.'''
      _sum = 0
      while not num == 0:
           _sum += num % 10 
           num = num // 10
      return _sum
number = int(input("insert the number: "))
print(f" the sum of my {number}'s digits is equal to: {sum_of_digits(number)}")
