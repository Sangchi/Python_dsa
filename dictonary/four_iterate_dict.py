'''
4. Write a Python program to iterate over dictionaries using for loops.

'''
def iterate_dict(dict):

    for key,value in dict.items():
        result=f"key:{key},value:{value}"
        print(result)

    
item_dict={0:10,1:20,2:30,3:40}

iterate_dict(item_dict)

'''
output-
key:0,value:10
key:1,value:20
key:2,value:30
key:3,value:40

'''