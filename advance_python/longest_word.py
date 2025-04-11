# Function to find the longest word in a sentence

def to_longest_word(str1):
    list1 = str1.split()
    max_word = ""

    for word in list1:
        if len(word) > len(max_word):
            max_word = word

    return max_word

str1 = input("Enter a sentence: ")
print("The longest word is:", len(to_longest_word(str1)))
