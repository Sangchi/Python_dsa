'''
13. Write a Python program to append a list to the second list.

'''


def append_list_to_another(list1, list2):
    
    list1.extend(list2)
    return list1

item_list1=[1,2,3]
item_list2=[4,5,6]
print(append_list_to_another(item_list1,item_list2))

'''
[1, 2, 3, 4, 5, 6]

'''