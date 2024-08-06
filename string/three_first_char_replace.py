'''
3. Write a Python program to get a string from a given string where all occurrences of its
first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'

'''
def char():
    user_input=input("enter the string:")
    first_char=user_input[0]
    result=first_char +user_input[1:].replace(first_char,"$")
    print(result)

char()

'''
enter the string:restart
resta$t

'''