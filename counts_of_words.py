'''this projects counts how many times a word written in file.'''
my_file = open('file.txt', 'r')
my_file = my_file.read()
names = my_file.split()
my_dict = {'word1': 1}
for ind in range(len(names)):
       count = 1
       for ind1 in range(ind + 1, len(names)):
                   if names[ind] == names[ind1]:
                          names.remove(ind + 1)
                          count += 1
       my_dict[f'word{ind}'] = count
print(my_dict)
