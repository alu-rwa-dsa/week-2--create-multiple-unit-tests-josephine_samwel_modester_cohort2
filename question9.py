# Authors: Samwel, Josephine, Modester
# GitHub handles: @Sammyiel, @Josephine-uwizeye, @Modester-mw

# Question:Input 2 lists - listA with n elements and listB which has all
# elements of listA except one (but the rest are in the same order).
# Outputs the missing element. E.g. f([8,1,2,3],[8,1,3]) outputs 2

list1 = []
n = int(input("Enter number of elements of list 1: "))
for i in range(0, n):
    element_list1 = int(input("Enter elements of your list 1: "))
    list1.append(element_list1)  # appending the elements

list2 = []
m = int(input("Enter number of elements of list 2: "))  # f([8,1,2,3],[8,1,3])
for i in range(0, m):
    element_list2 = int(input("Enter elements of your list 2: "))
    list2.append(element_list2)  # appending the elements
missing_element = list(set(list1) - set(list2))
print(missing_element)
