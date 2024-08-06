'''
8. Write a Python program to create set difference.

'''
def set_diffrence(set1,set2):

    difference1 = set1 - set2
    difference2 = set1.difference(set2)
    print("Difference using '-' operator:", difference1)
    print("Difference using '.difference()' method:", difference2)


    result=set1.difference(set2)

    print(result)

item_set1 = {1, 2, 3, 4, 5}
item_set2 = {4, 5, 6, 7, 8}

set_diffrence(item_set1,item_set2)

'''
output-
Difference using '-' operator: {1, 2, 3}
Difference using '.difference()' method: {1, 2, 3}
{1, 2, 3}



'''

