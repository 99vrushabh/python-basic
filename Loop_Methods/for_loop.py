# dict in FOR LOOP
from operator import index
from os import makedirs
import string


# FOR LOOP
player = ["kohli", "dhoni", "ronaldo", "werner"]

for item in player:
    print(item + "he is play very well")

# range fuction in for loop
for i in range(1, 9):
    print(i)

# break statment in for loop
# this statment use to break a loop
for i in range(9):
    print(i)
    if i == 5:
        break
else:
    print("the loop is end now")


# continue statment
# this statment use to skip vakue
for i in range(9):
    if i == 5:
        continue
    print(i)
else:
    print("the loop is end now")

# pass statment
# this statment's value is null
for i in range(5):
    print(i)
    if i == 2:
        pass
else:
    print("the loop3 is end now")

# multiplication table in for loop
num=int(input("enter number for multiplication number"))
for i in range(1,11):
    # print(str(num) + "*" + str(i) + "=" + str(i*num))

# f string
    print(f"{num}X{i}={num*i}")

# new
l1=["harry","sidhu","sam","leaderbridge"]
print(l1)
for name in l1:
    if name.startswith("s"):
        print(name,": congratulation you are selected")

# prime number
num=int(input("enter number :"))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False
        break
if prime:
    print(num," is prime value")
else:
    print(num," is not prime value")
dict = {
    "mitchell": 543,
    "kohli": 420,
    "sam": 190,
    "tom":90,
}
for marks, value in dict.items():
    print(marks,"\nyou get the",value, "marks")
    if value > 500:
        print(marks ,"\ncongratulation!\nyou have achived a+ grade")
    elif value > 400:
        print(marks ,"\ncongratulation!\nyou have achived b+ grade")
    elif value < 200 and value > 100:
        print(marks ,"\ncongratulation!\nyou are passed with c+ grade")
    else:
        print(marks ,"\ni am sorry! you are failed in this year")

# String in FOR LOOP    

string=input("enter your marks")
for value in string:
    print("\nyou get the",value, "marks")
    if value > 500:
        print("\ncongratulation!\nyou have achived a+ grade")
    elif value > 400:
        print("\ncongratulation!\nyou have achived b+ grade")
    elif value < 200 and value > 100:
        print("\ncongratulation!\nyou are passed with c+ grade")
    else:
        print("\ni am sorry! you are failed in this year")


