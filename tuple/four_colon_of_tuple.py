'''
4. Write a Python program to create the colon of a tuple.

'''
def create_slice_of_tuple(tpl, start, end):

    sliced_tuple = tpl[start:end]
    return sliced_tuple

original_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90)
start_index = 2
end_index = 5
result = create_slice_of_tuple(original_tuple, start_index, end_index)

print("Original Tuple:", original_tuple)
print("Sliced Tuple:", result)

'''
Original Tuple: (10, 20, 30, 40, 50, 60, 70, 80, 90)
Sliced Tuple: (30, 40, 50)
'''