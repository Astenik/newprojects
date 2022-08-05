'''this projects delets evry 3-rd element in the string'''
string = 'aswtewniwk'
new_string = ''
lst = []
new_string += string[0]
for ind in range(1,len(string)):
       if (ind + 1) % 3 != 0:
             new_string += string[ind]
print(new_string)
