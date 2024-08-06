'''
2. Write a Python program to reverse the order of the items in the array.

'''
import array as arr
def reverse_array(array):
    
    result=array[::-1]
    return result

array_data=arr.array("i",(1,2,3,4,5,6,7))
print(reverse_array(array_data))


'''
output-
array('i', [7, 6, 5, 4, 3, 2, 1])

'''