'''
10. Write a Python program to print a specified list after removing the 0th, 4th and
5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']

'''
def remove_specific_item(my_list):
    
    indices_to_remove = [5, 4, 0]

    for index in indices_to_remove:
        if index < len(my_list):
            my_list.pop(index)

    return my_list


sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
result = remove_specific_item(sample_list)
print(result)


'''
output-
['Green', 'White', 'Black']

'''
