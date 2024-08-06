'''
1. Write a Python script to sort (ascending and descending) a dictionary by
value.

'''

my_dict = {
    'apple': 3,
    'banana': 1,
    'cherry': 2,
    'date': 4
}

sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Original Dictionary:", my_dict)
print("Sorted by Value (Ascending):", sorted_asc)
print("Sorted by Value (Descending):", sorted_desc)

'''
Original Dictionary: {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}Sorted by Value (Ascending): {'banana': 1, 'cherry': 2, 'apple': 3, 'date': 4}
Sorted by Value (Descending): {'date': 4, 'apple': 3, 'cherry': 2, 'banana': 1}

'''