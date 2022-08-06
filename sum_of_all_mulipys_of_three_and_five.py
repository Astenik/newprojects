def sum_of_all_mulipys_of_three_and_five(length_of_interval):
          '''this function counts sum of all mulipys of three and five in interval.'''
          sum = 0
          for num in range(1, length_of_interval):
              if (num % 3 == 0) or (num % 5 == 0):
                  sum += num
          return sum 
print(sum_of_all_mulipys_of_three_and_five(1001))
