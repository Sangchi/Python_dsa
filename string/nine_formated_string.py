'''
9. Write a Python program to display formatted text (width=50) as output.

'''
def formated_string(text,width):
    lefaligned=text.ljust(width)
    rightaligned=text.rjust(width)
    centeraligend=text.center(width)

    print(f"leftaligend text:{lefaligned}")
    print(f"rightaligend: {rightaligned}")
    print(f"centerd : {centeraligend}")


sample_text="shanatnu-bansal"
size=50
formated_string(sample_text,size)
