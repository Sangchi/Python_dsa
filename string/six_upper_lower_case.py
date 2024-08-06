'''
6. Write a Python script that takes input from the user and displays that input back in
upper and lower cases.

'''
def upper_lower_case(user_input):
    result1=user_input.upper()
    result2=user_input.lower()

    print(f"upper_case_string is {result1}")
    print(f"lower case string is {result2}")

inputt=input("enter the string")

upper_lower_case(inputt)

'''
enter the stringPRashaNT
upper_case_string is PRASHANT
lower case string is prashant

'''