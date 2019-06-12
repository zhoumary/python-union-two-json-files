# Python program to find the missing
# and additional elements

# examples of lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

# prints the missing and additional elements in list2
print("Missing values in second list:", (set(list1).difference(list2)))
print("Additional values in second list:", (set(list2).difference(list1)))

# prints the missing and additional elements in list1
print("Missing values in first list:", (set(list2).difference(list1)))
print("Additional values in first list:", (set(list1).difference(list2)))

test = [i for i, j in zip(list1, list2) if i == j]
test01 = set(list1) & set(list2)
print test
print test01