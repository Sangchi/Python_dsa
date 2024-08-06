'''
8. Write a Python program to remove an item from a tuple.

'''
def remove_item(item_tuple, value):

    temp_list = list(item_tuple)
    if value in temp_list:
        temp_list.remove(value)
    new_tuple = tuple(temp_list)

    return new_tuple


item_tuple = (1, 2, 3, 4, 6)
result = remove_item(item_tuple, 2)
print(result)

'''
output-
(1, 3, 4, 6)

'''
