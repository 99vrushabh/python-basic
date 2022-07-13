# create list using []
from re import A


a = [1, 2, 3, 12, 32]
print(a)

a[0] = 80
print(a)
print(a[0])

# creat a list for all datatypes
b = [45, "hello", 4.5, False]
print(b)
print(type(b))


# list slice

print(b[1:3])

# list method
list = [1, 5, 9, 2, 4, 6]
print(list)

# 1 sort
list.sort()
print(list)

# 2 revers
list.reverse()
print(list)

# 3 append
list.append(8)
print(list)

# 4 insert
list.insert(5, 500)
print(list)

# 5 pop
list.pop(2)
print(list)

# 6 remove
list.remove(9)
print(list)

# 1
a=input("enter your name")
print("good Afternoon" + a)
# 2

a="this is very nice  place"
a.find("  ")
print(a)
