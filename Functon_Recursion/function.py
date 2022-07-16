# user define function
from itertools import product
from math import factorial


def result(marks):
    p = ((marks[0]+marks[1]+marks[2]+marks[3]+marks[4])/5)
    return p


percentage = [45, 50, 54, 45, 74]
form = result(percentage)
print(form)

percentage2 = [89, 87, 77, 52, 60]
form = result(percentage2)
print(form)

# to greet the people


def greet(name):
    print("good day", name)


a = input("enter your name")
greet(a)
# defult value function


def greet(name='vrushabh'):
    print("good day", name)


greet()

# recursion
# fectorial numbers
number = 6
product = 1
for i in range(number):
    product = product*(i+1)
print(product)

# fectoril numbers using function
def fectorial(n):
    product = 1
    for i in range(number):
        product = product*(i+1)
    return product
print(factorial(4))


# defult value function
def d_value(x,y=50):
    print("x: ",x)
    print("Y: ",y)

d_value(10)

def student(firstname, lastname): 
     print(firstname, lastname)
 

student("vrushabh","gohil")
