'''
12. Write a Python program to check multiple keys exists in a dictionary.

'''
def are_keys_present(dictionary, keys):

    return all(key in dictionary for key in keys)

sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

keys_to_check = ['a', 'b', 'c']
result = are_keys_present(sample_dict, keys_to_check)
print("All keys present:", result)  

keys_to_check = ['a', 'b', 'x']
result = are_keys_present(sample_dict, keys_to_check)
print("All keys present:", result)

'''
output-
All keys present: True
All keys present: False

'''
