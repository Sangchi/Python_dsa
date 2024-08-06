'''
1. Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.

'''
import array as arr
def create_array():

    result=arr.array("i",(1,2,3,4,5,6))

    return result

print(create_array())

'''
output-
array('i', [1, 2, 3, 4, 5, 6])

'''