'''
9. Write a Python program to print a dictionary in table format.

'''
from prettytable import PrettyTable

def print_dict_in_table(dictionary):

    table = PrettyTable()
    table.field_names = ["Key", "Value"]
    for key, value in dictionary.items():
        table.add_row([key, value])
    print(table)

my_dict = {
    "Name": "John Doe",
    "Age": 30,
    "Occupation": "Software Developer",
    "Location": "New York"
}

print_dict_in_table(my_dict)

'''
output-
+------------+--------------------+
|    Key     |       Value        |
+------------+--------------------+
|    Name    |      John Doe      |
|    Age     |         30         |
| Occupation | Software Developer |
|  Location  |      New York      |
+------------+--------------------+

'''


