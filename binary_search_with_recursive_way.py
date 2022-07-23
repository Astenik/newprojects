def binary_search_rec(lst, key, start, end):
       '''this function finds key in the list if it is else return -1
       my function have 4 argument where the first argument is the list
       the second argument is the key the third argument is the start of my list
       and the 4-rd argument is the end of my list.'''
       if start > end:
            return -1 
       mid = (start + end) // 2
       if lst[mid] == key:
            return mid
       if key > lst[mid]:
            s = mid + 1
            return binary_search_rec(lst, key, s, end) 
       else:
            e = mid - 1
            return binary_search_rec(lst, key, start, e)
lst = [12, 45, 89, 90, 5363]
key = int(input("insert the key: "))
end = int(input("insert length of your list: "))
print(f"{key}'s position in the {lst} is: {binary_search_rec(lst, key, 0, end)}")
