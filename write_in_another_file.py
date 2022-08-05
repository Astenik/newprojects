 '''this project reads all the text from file.txt file and write it in a new file changeing all words first letters uppercase.'''
my_file = open('file.txt', 'r')
my_file = my_file.read()
nums = my_file.split()
new_file = open('file2', 'w')
new_file = new_file.write(my_file.title())
open('file2', 'r')
