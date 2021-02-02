# Authors: Samwel, Josephine, Modester
# GitHub handles: @Sammyiel, @Josephine-uwizeye, @Modester-mw

# Question: Input a list of lists and return a single list with each element occurring exactly once.

# defining a function that takes a list of list sums up the lists into a single list and using
# list and set to remove duplicates

def list_of_list():
    fruits = [["mango", "pineapple"], ["pineapple", "guava"]]
    result = (sum(fruits, []))
    print(list(set(result)))

    # calling out the function


list_of_list()

