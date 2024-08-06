'''
3. Write a Python program to get the smallest number from a list

'''

def smallest_element(list):

    min=list[0]
    for i in list:
        if i < min:
            min=i

    return min

item_list=[2,4,5,-1]
print(smallest_element(item_list))


