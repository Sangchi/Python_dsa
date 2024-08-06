'''
14. Write a python program to check whether two lists are circularly identical.

'''
def are_circularly_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    
    concatenated_list1 = list1 + list1
    for i in range(len(list1)):
        if concatenated_list1[i:i + len(list2)] == list2:
            return True
    
    return False

list1 = [1, 2, 3, 4]
list2 = [3, 4, 1, 2]

print(are_circularly_identical(list1, list2))

list3 = [1, 2, 3, 4]
list4 = [4, 3, 2, 1]

print(are_circularly_identical(list3, list4))

'''
output-

True
False

'''

