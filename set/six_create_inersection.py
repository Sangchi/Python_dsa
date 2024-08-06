'''
6.Write a Python program to create an intersection of sets.

'''

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

intersection1 = set1 & set2
intersection2 = set1.intersection(set2)

print("Intersection using '&' operator:", intersection1)
print("Intersection using '.intersection()' method:", intersection2)


'''
output-
Intersection using '&' operator: {4, 5}
Intersection using '.intersection()' method: {4, 5}

'''