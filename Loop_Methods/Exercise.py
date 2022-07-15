# for numbers 1 to 10
from audioop import reverse
from math import factorial


print("for numbers 1 to 10")
i=0
while i<11:
    print(i)
    i=i+1

# for star method
print("star method")
for i in range(0,6):
    for j in range(0,6):
        if j<=i:
            print("*",end='')
    print(" ")

# sum method
print("sum method")

s=0
i=int(input("enter your number\n"))

for i in range(1,i+1,1):
    s+=i
    print("sum is ",s)

# multiplication table
print("multiplication table")

i=int(input("enter your number\n"))
for s in range(1,11,1):
    table=s*i
    print("the value is",table)


# for get some numbers from list
print("get some numbers from list")

numbers = [12, 75, 150, 180, 145, 525, 50]

for item in numbers:
    if item>500:
        break
    elif item>150:
        continue
    elif item % 5 ==0:
        print(item)

# revers star method
print("revers star method")

for i in range(0,6):
    for j in range(0,6):
        if j>=i:
            print(j+1,end='')
    print(" ")


# print list in revers method using loop
print("list in revers method using loop")

list1 = [10, 20, 30, 40, 50]
new_list=reversed(list1)
for new_list in reversed(list1):
        print(new_list)

# print revers number
print("revers number -10 to -1")

i=0
for a in range(-10,0,1):
    print(a)


# successfully and of loop
for i in range(5):
    print(i)
i == range(5)
print("done!")

# fectorial method
num=3
factorial = 1
for i in range(1, num+1):
        result = factorial * i
        print("The factorial of", num, "is", result)
# sum
s=0
i=int(input("enter number"))
for i in range(1,i+1):
    s+=i
    print(s)


# revers number


# odd number
print("odd number")
i=[10,20,30,40,50,60]
for lost in i[1: :2]:
    print(lost)

# even number
print("even number")
for lost in i[0: :2]:
    print(lost)

# cube of enter number by user



# cube for try
cube=int(input("enter"))
for i in range(1,cube+1):
    print("the current number is :",i,"cube is",(i*i*i))

# half daimond
for i in range(0,6):
    for j in range(0,6+1):
        if j<=i:
            print("*",end='')
    print(" ")
for i in range(0,6):
    for j in range(0,6+1):
        if j>=i:
            print("*",end='')
    print(" ")
sampleDict = dict([
    ('first', 1),
    ('second', 2),
    ('third', 3)
])
print(sampleDict)