def odd_nums(num1, num2):
      '''this function returns count of odd numbers in interval (num1, num2) 
      where num1 and num2 are the arguments of this function'''
      ind = num1
      count = 0
      while ind <= num2:
            if ind % 2 != 0:
                 count += 1
            ind += 1 
      return count

print(odd_nums(1, 9))
