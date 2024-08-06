'''
10. Write a Python program to count the values associated with key in a
dictionary.
Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
Expected result: Count of how many dictionaries have success as True

'''
def count_success_true(data, key='success'):
    
    
    true_count = 0
    for item in data:
        if item.get(key) is True:
            true_count += 1

    return true_count

data = [
    {'id': 1, 'success': True, 'name': 'Lary'},
    {'id': 2, 'success': False, 'name': 'Rabi'},
    {'id': 3, 'success': True, 'name': 'Alex'}
]

result = count_success_true(data)
print("Count of how many dictionaries have 'success' as True:", result)

'''
output-
Count of how many dictionaries have 'success' as True: 2

'''