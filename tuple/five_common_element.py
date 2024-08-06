'''
5. Write a Python program to find the repeated items of a tuple.


'''
def repeated_element(list):
    
    result=[]
    common=[]
    for i in list:
        if i not in result:
            result.append(i)
        else:
            common.append(i)

    return common

item_list=[1,2,3,4,5,6,1,2,5,6]
print(repeated_element(item_list))

'''
output-
[1, 2, 5, 6]


'''
