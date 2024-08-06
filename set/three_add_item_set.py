'''
3. Write a Python program to add member(s) in a set.

'''

def add_item_to_set(my_set, item):
    
    my_set.add(item)
    return my_set

item_set = {1, 2, 3, 4, 5}

new_item = 6
updated_set = add_item_to_set(item_set, new_item)
print(updated_set)

'''
output-
{1, 2, 3, 4, 5, 6}

'''
