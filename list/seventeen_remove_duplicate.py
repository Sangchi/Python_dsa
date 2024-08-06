'''
17. Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]

'''
def remove_duplicates(list_of_lists):

    seen = set()
    result = []
    
    for sublist in list_of_lists:
        tuple_sublist = tuple(sublist)
        if tuple_sublist not in seen:
            seen.add(tuple_sublist)
            result.append(sublist)
    
    return result

list_of_lists = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
new_list = remove_duplicates(list_of_lists)

print("New List:", new_list)
