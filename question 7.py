# Authors: Samwel, Josephine, Modester
# GitHub handles: @Sammyiel, @Josephine-uwizeye, @Modester-mw

#Question: Input a string and return a dictionary with the number of occurrences of each
# character in the string. E.g. f(“hi”) outputs {‘h’:1,’i’:1}

def countcharacters(text):
    dictionary = {}
    for character in text:
        if character not in dictionary:
            dictionary[character] = 1
        else:
            dictionary[character] += 1
    return dictionary
x = input("enter your string")
print(countcharacters(x))


