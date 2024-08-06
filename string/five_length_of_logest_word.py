'''
5. Write a Python function that takes a list of words and returns the length of the longest
one.

'''
def length_of_logest_word(worldlist):
    max_length=0
    max_world=""
    for world in worldlist:
        if(len(world)>max_length):
            max_length=len(world)
            max_world=world

    return f"the maxlenth is={max_length},the max word is ={max_world}"

word=["apple","banana","mango","dragonfruit"]

print(length_of_logest_word(word))

'''
output-
the maxlenth is=11,the max word is =dragonfruit

'''