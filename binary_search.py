def bin_search(lst, key):
       '''this function finds key in the list if
       the list sorted in ascending order.'''
       start = 0
       end = len(lst) - 1 
       while start <= end:
            mid = (start + end) // 2
            if lst[mid] == key:
                  return mid
            if key > lst[mid]:
                 start = mid + 1
            else:
                  end = mid - 1
       return -1
key = int(input("insert the key: "))
list = [12, 45, 67, 90, 1256]
print(f''the {key}'s position in the {list} is: {bin_search(list, key)}')
