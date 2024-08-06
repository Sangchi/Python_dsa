'''
11. Write a Python program to generate all permutations of a list in Python.

'''
import itertools

def generate_permutations(lst):
    
    permutations = list(itertools.permutations(lst))
    return permutations

sample_list = [1, 2, 3]


permutation = generate_permutations(sample_list)
for perm in permutation:
    print(perm)


'''
output-

(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)

'''