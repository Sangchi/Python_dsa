'''
4. Write a Python program to remove item(s) from set

'''

def remove_item_from_set(my_set, item):

    my_set.discard(item)
    print(f"Item {item} removed using discard().")
    return my_set

item_set={1,2,3,4,5}
remove_elment=3
print(remove_item_from_set(item_set,remove_elment))

'''
output-
{1, 2, 4, 5}

'''