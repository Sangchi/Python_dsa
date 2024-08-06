'''
3. Write a Python program to unpack a tuple in several variables.

'''
def unpack_tuple():

    my_tuple = (10, 'Hello', 3.14, True)
    num, greeting, pi, flag = my_tuple
    return num, greeting, pi, flag

num, greeting, pi, flag = unpack_tuple()

print("Number:", num)
print("Greeting:", greeting)
print("Pi:", pi)
print("Flag:", flag)

'''
Number: 10
Greeting: Hello
Pi: 3.14
Flag: True

'''
