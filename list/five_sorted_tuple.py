'''
5. Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''
# def sorted_by_last_element(tuples_list):
    
#     return sorted(tuples_list, key=lambda x: x[-1])

# item_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# print(sorted_by_last_element(item_list))


# '''
# output-

# [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# '''

def bubble_sort_last_element(tuples_list):

    n = len(tuples_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if tuples_list[j][-1] > tuples_list[j+1][-1]:
                tuples_list[j], tuples_list[j+1] = tuples_list[j+1], tuples_list[j]
    return tuples_list

item_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(bubble_sort_last_element(item_list))


























