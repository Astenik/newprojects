def is_polindrom(number):
        '''this function retturns true if 
        the number is polindrom. 
        number is the argument of function.'''
        num = 0
        cpy_number = number
        while number != 0:
               num *= 10
               num += number % 10
               number = number // 10
        return num == cpy_number 
number = int(input("insert number: "))
print(f'is your number a polindrom? {is_polindrom(number)}')
