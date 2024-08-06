'''
12. Write a Python program to lowercase first n characters in a string

'''

def n_lower_case(string,n):
    
    if n>len(string):
        n=len(string)

    lower_case=string[:n].lower()
    remaing_string=string[n:]

    return lower_case +remaing_string

user_input=input("enter the input:")
n_number=int(input("enter number of elment to lower_case:"))

print(n_lower_case(user_input,n_number))


'''
output-
enter the input:PRASHANT
enter number of elment to lower_case:3
praSHANT

'''