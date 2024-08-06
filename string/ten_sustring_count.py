'''
10. Write a Python program to count occurrences of a substring in a string.

'''

def substring_count(string, substring):

    count = 0
    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += len(substring)
    
    return count

text = "prashantpra"
substring = "pra"
print(substring_count(text, substring))


