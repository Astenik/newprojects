def new_list(lst):
      ''' this function returns new list that consists of quados of members of lst list and is sorted.'''
      lst1 = []
      for ind in range(len(lst)):
           for ind1 in range(ind + 1, len(lst)):
                  if lst[ind] > lst[ind1]:
                        lst[ind], lst[ind1] = lst[ind1], lst[ind]
      for num in lst:
             lst1.append(num**2)
      return lst1 
print(new_list([3, 4, 5, 2, 1]))
