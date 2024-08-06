'''
16. Write a Python program to split a list based on first character of word.

'''
from collections import defaultdict


def split_list_by_first_char(words):

    result = defaultdict(list)
    for word in words:
        if word:
            result[word[0].upper()].append(word)
    
    return dict(result)

words = ['apple', 'banana', 'apricot', 'blueberry', 'avocado', 'blackberry']
split_words = split_list_by_first_char(words)

print("Words split by first character:")
for char, words in split_words.items():
    print(f"{char}: {words}")



'''
output-
Words split by first character:
A: ['apple', 'apricot', 'avocado']
B: ['banana', 'blueberry', 'blackberry']

'''
