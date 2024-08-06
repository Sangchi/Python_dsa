'''
2. Write a Python program to count the number of characters (character frequency) in a
string.
Sample String : google.com
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

'''
def charcount():
    user_input=input("enter the string:")
    data={}
    for char in user_input:
        if char in data:
            data[char] +=1

        else:
            data[char]

    print(data)

charcount()

'''
output-
enter the string:google.com
{'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
'''