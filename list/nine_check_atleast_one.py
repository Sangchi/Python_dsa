'''
9. Write a Python function that takes two lists and returns True if they have at
least one common member.

'''
def atleast_one_ele_in_list(list):

    if len(list)>=1:
        return True
    
    return False

item_list=[]
print(atleast_one_ele_in_list(item_list))

'''
output-
False

'''