'''
6. Write a Python program to check whether an element exists within a tuple.

'''
def element_exist(tuple,element):

    for i in tuple:
        if i==element:

            return "element exist"
        
    return "element not exit"

item_tuple=(1,2,3,5,6)
n=int(input("enter the number:"))
print(element_exist(item_tuple,n))


'''
output-
enter the number:3
element exist

'''
