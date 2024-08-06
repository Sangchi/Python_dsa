'''
6. Write a Python program to remove duplicates from a list.

'''
def remove_duplicaate(list):
    
    result=[]
    for i in list:
        if i not in result:
            result.append(i)

    return result

item_list=[1,2,4,3,5,4,2,1,7,8]
print(remove_duplicaate(item_list))


'''
output-
[1, 2, 4, 3, 5, 7, 8]

'''
