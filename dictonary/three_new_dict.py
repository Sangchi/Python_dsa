'''
3. Write a Python script to concatenate following dictionaries to create a new
one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


'''
def conacatinate_dict(dict1,dict2,dict3):

    new_dict={**dict1,**dict2,**dict3}
    return new_dict

item_dict_one={1:10, 2:20}
item_dict_two={3:30, 4:40}
item_dict_three={5:50,6:60}

print(conacatinate_dict(item_dict_one,item_dict_two,item_dict_three))

'''
output-
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

'''