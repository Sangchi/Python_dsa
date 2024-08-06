'''

2. Write a Python program to multiplies all the items in a list.

'''
def multiplay_list(list):

    multiplication=1
    for i in list:
        multiplication *=i

    return f"listmultiplication is :{multiplication}"

item_list=[1,2,3,4,5]
print(multiplay_list(item_list))

'''
listmultiplication is :120

'''