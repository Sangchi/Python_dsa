'''
6. Write a Python program to remove a key from a dictionary.

'''
def remove_key(input_dict, key_to_remove):

    if key_to_remove in input_dict:
        del input_dict[key_to_remove]
    else:
        return "Key not found"
    
    return input_dict

item_dict = {1: 20, 2: 30, 3: 40}
key = 2
print(remove_key(item_dict, key))

'''
output-
{1: 20, 3: 40}
'''

