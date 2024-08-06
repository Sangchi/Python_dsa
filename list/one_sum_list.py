'''
1. Write a Python program to sum all the items in a list.

'''
def sumlist(list):

    sum=0
    for i in list:
        sum +=i

    return f"sum is:{sum}"
item_list=[1,2,3,4,5]
print(sumlist(item_list))

'''
output-
sum is:15

'''