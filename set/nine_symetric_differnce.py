'''
9. Write a Python program to create a symmetric difference.

'''

def symetric_difference(set1,set2):

    symmetric_difference1 = set1 ^ set2
    symmetric_difference2 = set1.symmetric_difference(set2)
    return f"Symmetric difference using '^' operator:{symmetric_difference1}",f"Symmetric difference using '.symmetric_difference()' method: {symmetric_difference2}"


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(symetric_difference(set1,set2))


'''
output-
("Symmetric difference using '^' operator:{1, 2, 3, 6, 7, 8}", "Symmetric difference using '.symmetric_difference()' method: {1, 2, 3, 6, 7, 8}")

'''



