'''
4. Write a Python program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the

given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'

'''
def add_ing():
    user_input = input("Enter the string: ")
    
    if len(user_input) < 3:
        print(user_input)
    elif user_input.endswith("ing"):
        user_input += "ly"
        print(user_input)
    else:
        user_input += "ing"
        print(user_input)

add_ing()

'''
Enter the string: string
stringly

'''

def add_ing():
    user_input = input("Enter the string: ")
    
    if len(user_input) < 3:
        print(user_input)
    else:
        if(len(user_input)>=3)and (user_input[-3:]=="ing"):
            user_input += "ly"
            print(user_input)
        else:
            user_input += "ing"
            print(user_input)

add_ing()

'''
Enter the string: string
stringly
'''

