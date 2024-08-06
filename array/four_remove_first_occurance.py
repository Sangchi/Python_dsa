'''
4. Write a Python program to remove the first occurrence of a specified element from an
array.

'''
import array as arr

def remove_element(array,element):
    
    for i in array:
        if i==element:
            array.remove(element)

    return array
array_data=arr.array("i",(1,2,3,4,5,6))
element_to_remove=2

print(remove_element(array_data,element_to_remove))

'''
output-
array('i', [1, 3, 4, 5, 6])

'''