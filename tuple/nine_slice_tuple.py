'''
9. Write a Python program to slice a tuple.

'''

def slice_tuple(tuple):

    result=tuple[1:]
    return result

item_tuple=(1,2,3,4,5,6)
print(slice_tuple(item_tuple))

'''
output-
(2, 3, 4, 5, 6)

'''