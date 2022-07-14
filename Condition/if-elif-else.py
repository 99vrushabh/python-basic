
from tkinter import N
from unicodedata import name
from xml.dom.minidom import Element

# it's a ladder in py
a =int( input("enter your marks"))
if(a > 50):
    print("the value is higher")
elif(a < 50):
    print("the value is < 50")
elif(a < 50):
    print("the value is < 50")
else:
    print("this value in not valid")


# multiple if statement
a =int( input("enter your marks"))
if(a<100):
        print("one")
if(a>50):
    print("two")

# # relatonal oprators
a=int(input("enter your age"))
if(a >= 18):
    print("yes")
else:
    print("no")

# # logical oprators
a=int(input("enter your age"))
if(a>50 and a<100):
    print("you are aligible")
else:
    print("you are not aligible")

# # in and is method
# # is
a=None
if(a is None):
    print("yes")
else:
    print("no")

# # in
a=[545,41,42,46]
print(545 in a)

# find the gretest number enter by the user
num1 = int(input("enter number 1 :  "))
num2 = int(input("enter number 2 :  "))
num3 = int(input("enter number 3 :  "))
num4 = int(input("enter number 4 :  "))

if(num1 > num2):
    f1 = num1
else:
    f1 = num2

if(num3 > num4):
    f2 = num3
else:
    f2 = num4

if(f1 > f2):
    print(f1, "is greter")
else:
    print(f2, "is greater")

# make result for student for pass or fail
m1 = int(input("enter your marks\n"))
m2 = int(input("enter your marks\n"))
m3 = int(input("enter your marks\n"))


if(m1 < 33 or m2 < 33 or m3 < 33):
    print("you have not reached at 33 marks so you are fail")
elif(m1+m2+m3)/3 < 40:
    print("you are faild because you result was under 40% ")
else:
    print("you are passed!")

# or in this condition onther way to sovle, try this-->

if(m1 < 33 or m2 < 33 or m3 < 33) or (m1+m2+m3)/3 < 40:
    print("you have not reached at 33 marks so you are fail")
else:
    print("you are passed!")

a=["werner","wright","ronaldo","kohli"]
name=input("enter your name to check it")
if name in a:
    print("you are in list")
else:
    print("you are not in list")

# for get a grade form user's marks
marks = int(input("enter your marks to get a grade"))
if marks >= 90:
    print("EX")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("error")

    a=1000
    b=2500
    print(a)
    print(b)
    print(a+b)

