'''
12. Write a Python program to get the difference between the two lists.

'''

def difference_between_lists(list1, list2):
    
    set1 = set(list1)
    set2 = set(list2)
    difference = set1 - set2
    result = list(difference)
    return result

list_item1 = [1, 2, 3, 4, 5]
list_item2 = [1, 2, 3, 4, 5]

print(difference_between_lists(list_item1, list_item2))

'''
output-
[]


'''
