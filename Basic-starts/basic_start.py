from tkinter.tix import INTEGER
from winsound import PlaySound
from xml.etree.ElementTree import Comment
import os



#  for'for multi line comment
''' single line Comment
'''

# for multi line print so use in triple string
      
# print('''def do_some(seconds, my_var):
#       print(f'Sleep {seconds} seconds... my variable {my_var}')
#       time.sleep(seconds)
#       print('Done sleep...)''')

# # onlistdir
# print(os.listdir())

# # variables
a="admin" #this is string 
b=345 #this is integer
c=45.7 #this is float

# '''variable is container to store a value'''
# '''kewwords is reserved wors in python like: def'''
# '''identifiers is class/variables name'''

# datatype
# INTEGER{....-3,-2,-1,0,1,2,3........}
# string{"hello"} also {'''hello'''}
# floating point number{1.2,2.5,6.1....}
# boolines{true or false}
# none

__a123='''hello "world"'''
b=1323 
c=2.2

print(__a123)
print(b)
print(c)

# printing the diffrent type of variables

print(type(__a123))
print(type(b))
print(type(c))

# opraters
# arithmatic oprater => + - * /;
# asssignment oprator => = +- -= -+
# comperission oprator => = > < != <= >=    
# logical oprator => and or not


a=2
b=6
#  arithmatic oprater
print("this is value of 2+6=",a+b)
print("this is value of 2+6=",a-b)
print("this is value of 2+6=",a*b)
print("this is value of 2+6=",a/b)


# assignment oprator
a=50
a/=2
# a*=2
# a-=2
print(a)

# comperission opretors
b=6<7
print(b)
b=7<=7
print(b)
b=8!=7
print(b)

# logical opretors
a=True
b=False
print("the value of  a and b is",a and b)
print("the value of  a or b is",a or b)
print("the value of  not  b is",not b)
# type
# for type of any variable
# typecasting
# for convert string to int. use typecasting
a="3434"
print(a)
# # conv. into int.
a=int(a)
# # conv. into float
a=float(a)
print(a)

print(a+5)


a=21
b="23"
c=21
print(str(a))
print(int(b))
print(float(c))
a = input("first number:")
b = input("second number:")
a=int(a)
b=int(b)

print("the value of a+b is", a + b)

# 2
a = 10
b = 4
avg=((a+b)/2)
print("the value of a+b is", avg)
a=1000
b=2500
print(a)
print(b)
print("the value of a+b is ",a+b)



