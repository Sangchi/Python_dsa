'''
5. Write a Python program to remove an item from a set if it is present in the set.

'''
def remove_specific_item(s, specific_item):
    s.discard(specific_item)
    return s


my_set = {1, 2, 3, 4, 5}
item_to_remove = 3

print("Original set:", my_set)
my_set = remove_specific_item(my_set, item_to_remove)
print("Set after removal:", my_set)


'''
Original set: {1, 2, 3, 4, 5}
Set after removal: {1, 2, 4, 5}

'''