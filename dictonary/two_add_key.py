'''
2. Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}

'''
def add_key(dict):

    new_key=2
    new_value=30
    dict[new_key]=new_value

    return dict

sample_dict={0:10,1:20}
print(add_key(sample_dict))