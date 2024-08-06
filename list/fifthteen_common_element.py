'''
15. Write a Python program to find common items from two lists.

'''
def find_common_items(list1, list2):
    
    set1 = set(list1)
    set2 = set(list2)
    common_items = set1 & set2
    return list(common_items)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print("Common items (using sets):", find_common_items(list1, list2))

'''
output-
Common items (using sets): [4, 5]


'''
