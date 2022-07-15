# dict in FOR LOOP
from operator import index
from os import makedirs
import string


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


