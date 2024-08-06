'''
11. Write a Python program to use of frozensets.

'''

frozenset1 = frozenset([1, 2, 3, 4, 5])
frozenset2 = frozenset([4, 5, 6, 7, 8])

print("Frozenset 1:", frozenset1)
print("Frozenset 2:", frozenset2)


# Intersection
intersection = frozenset1 & frozenset2
print("Intersection:", intersection)

# Union
union = frozenset1 | frozenset2
print("Union:", union)

# Difference
difference = frozenset1 - frozenset2
print("Difference:", difference)

# Symmetric Difference
symmetric_difference = frozenset1 ^ frozenset2
print("Symmetric Difference:", symmetric_difference)

try:
    frozenset1.add(9)
except AttributeError as e:
    print("Error:", e)


'''
Frozenset 1: frozenset({1, 2, 3, 4, 5})
Frozenset 2: frozenset({4, 5, 6, 7, 8})
Intersection: frozenset({4, 5})
Union: frozenset({1, 2, 3, 4, 5, 6, 7, 8})
Difference: frozenset({1, 2, 3})
Symmetric Difference: frozenset({1, 2, 3, 6, 7, 8})
Error: 'frozenset' object has no attribute 'add'

'''
