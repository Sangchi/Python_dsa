'''
8. Write a Python program to find the list of words that are longer than n from a
given list of words

'''
def longwords(word_list, n):
    
    result = []
    for word in word_list:
        if len(word) > n:
            result.append(word)

    return result

item_list = ["abc", "absc", "efghsk"]
n = 3
print(longwords(item_list, n))

'''
outout-
['absc', 'efghsk']

'''
