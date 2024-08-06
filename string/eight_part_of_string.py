'''
8. Write a Python program to get the last part of a string before a specified character.
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python

'''
def last_part_of_string(userinput,char):
    index=userinput.rfind(char)

    if index==-1:
        return userinput
    
    return userinput[:index]

input="https://www.w3resource.com/python-exercises"
char="-"
print(last_part_of_string(input,char))

'''
output-
https://www.w3resource.com/python
'''

