'''
7. Write a Python program that accepts a comma separated sequence of words as input
and prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red

'''
def process_words(input_string):
    
    words = input_string.split(",")
    
    unique_words = []
    seen = set()
    for word in words:
        word = word.strip()
        if word not in seen:
            unique_words.append(word)
            seen.add(word)
    
    sorted_words = sorted(unique_words)
    result = ",".join(sorted_words)
    
    return result

user_input = input("Enter a comma-separated sequence of words: ")

print(process_words(user_input))
