a={}
print(type(a))

# for empty set
b=set()
print(type(b))

a={1,2,3,4,5,1}
print(a)
print(type(a))


# set method
# 1 add
a.add(9)
a.add(12)
# also add a tuple but  not list,dictionary
# tuple
a.add((2,9,5))

# list
a.add("hello")
print(a)


# 2 lenght
print(len(a))
# 3 remove
b={1,2,3,4,5,6}
print(b)

b.remove(2)
print(b)

# pop
print(b.pop())

a=input("enter number: \n")
b=input("enter number: \n")
c=input("enter number: \n")
d=input("enter number: \n")
e=input("enter number: \n")
f=input("enter number: \n")
g=input("enter number: \n")

sum ={a,b,c,d,e,f,g}
print(sum)
