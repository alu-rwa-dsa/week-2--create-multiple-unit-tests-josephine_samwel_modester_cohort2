# Authors: Samwel, Josephine, Modester
# GitHub handles: @Sammyiel, @Josephine-uwizeye, @Modester-mw

# Question: Input an integer n and outputs a list with 1 once, 2 twice, 3 three times….n n-times e.g. f(3) = [1,2,2,3,3,3]

def multiplied_integers_list():
    counter = 0
    lst = []
    n = int(input("input any number!! "))
    for i in range(0, n):
        numbers = str(i) * i
        counter += 1
        lst.append(numbers)
        print(numbers)


multiplied_integers_list()
