'''
3. Write a Python program to get the number of occurrences of a specified element in an
array.

'''
import array as arr


def number_count(array,number):

    count=0
    for i in array:
        if i==number:
            count +=1

    return f"the number appear {count} time in array"
array_data=arr.array("i",(1,2,3,4,5,6,7,9,7,7))
given_number=7

print(number_count(array_data,given_number))


'''
output-
the number appear 3 time in array

'''