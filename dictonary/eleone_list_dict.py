'''
11. Write a Python program to convert a list into a nested dictionary of keys.

'''

def list_to_nested_dict(lst):
    
    if not lst:
        return {}

    nested_dict = {}
    current_level = nested_dict
    for item in lst:
        current_level[item] = {}
        current_level = current_level[item]

    return nested_dict

sample_list = ['a', 'b', 'c', 'd']
result = list_to_nested_dict(sample_list)
print(result)


'''
output-
{'a': {'b': {'c': {'d': {}}}}}

'''