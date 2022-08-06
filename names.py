'''this function write all the names in 
file.txt file to the file2 file, but all the
first letters of every names becomed uppercase.'''
file1 = open('file.txt', 'r')
new_file = open('file2', 'w')
file1 = file1.read()
new_file = new_file.write(file1.title())
