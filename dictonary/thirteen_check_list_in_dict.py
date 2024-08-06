'''
13. Write a Python program to count number of items in a dictionary value
that is a list.

'''

def count_items_in_lists(dictionary):
   
    total_count = 0
    for value in dictionary.values():
        if isinstance(value, list):
            total_count += len(value)

    return total_count

sample_dict = {
    'fruits': ['apple', 'banana', 'cherry'],
    'vegetables': ['carrot', 'broccoli'],
    'numbers': [1, 2, 3, 4],
    'name': 'John Doe'
}

result = count_items_in_lists(sample_dict)
print("Total number of items in list values:", result)

'''
output-
Total number of items in list values: 9

'''
