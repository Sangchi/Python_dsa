'''
7. Write a Python program to create a union of sets.

'''
def set_union(set1,set2):

    union_operation=set1 | set2
    return union_operation

set_item_one={1,2,3,4,5,6}
set_item_two={7,8,9,10,11}

print(set_union(set_item_one,set_item_two))

'''
output-

{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

'''