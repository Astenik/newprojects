def count_of_mem(lst):
     '''this function returns the counts of elements that are divaded their indexes.'''
     count = 0
     for ind in range(1, len(lst)):
          if lst[ind] % ind == 0:
                count += 1 
     return count 

print(f"the count of members that are divaded their indexes is equal to: {count_of_mem([90, 78, 6, 7, 12])}")
