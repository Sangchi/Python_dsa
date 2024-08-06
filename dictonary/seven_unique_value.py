'''
7. Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

'''
def add_unique_value(data):

    unique_value=set()
    for dict in data:
        for value in dict.values():
            unique_value.add(value)

    return unique_value

item_data= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print(add_unique_value(item_data))

'''
output-
{'S001', 'S002', 'S005', 'S007', 'S009'}

'''

