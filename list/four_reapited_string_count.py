'''
4. Write a Python program to count the number of strings where the string length
is 2 or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2

'''
def reapited_string_count(list):

    count=0
    for i in list:
        if len(i)>2:
            if i[0]==i[-1]:
                count +=1

    return f"count is={count}"

item_list=['abc', 'xyz', 'aba', '1221',"prp"]
print(reapited_string_count(item_list))

'''
output-
count is=3

'''
