# # simple example of return function  
# from unicodedata import name


# def add_number(a,b):
#     return(a+b)
# def check(a):
#     return bool(a)

# check_number=add_number(10,20)
# check_bool=check(2>6)

# print("the sum of this function is : ",check_number)
# print("the value of this function is : ",check_bool)

# # another way of return function
# def add_number(a,b):
#     total=a+b
#     return(total)
# def check(a):
#     boolien=a
#     return boolien

# check_number=add_number(100,20)
# check_bool=check(2<6)

# print("the sum of this function is : ",check_number)
# print("the value of this function is : ",check_bool) 

# # this return function set a method for main function and that var. never used 
# # give the greetings
# def greet(name):
#     details=name
#     return details
# final="hello!"+greet(input("enter your name"))
# print(final)

# # another way to sum numbers
# def once(x):
#     def second(y):
#         return x+y
#     return second
# final_value=once(float(input("enter 1st value for sum")))
# print("the final value is :" , final_value(float(input("enter 1st value for sum"))))

# new 

# first get a function and in that function run a loop
from unicodedata import name


def loopy(number):
    # for i in number:
    # import pdb
    # pdb.set_trace()
    if int(number) >= 500:
        i = "nice!"
    elif int(number)>= 350:
        i = "wonderfull!"
    else:
        i = "nice try!"
    return i

a=loopy((input("enter number:-")))
print(a)

def check_numbers(num1,num2):
    check_total=num1+num2
    return check_total
first=check_numbers(50,4)
print(first)


def func1(number):
    if number>=150:
        print("player of the match")
    elif number>=100:
        print("nice player")
    elif number>=75:
        print("avg. player")
    else:
        print("give more opp.")

func1(int(input("enter your 1st odi match score")))

def score_total(s1,s2,s3):
    match=s1+s2+s3
    return match
name=input("enter your name")
result=score_total(int(input("enter 1st odi's score")),int(input("enter 2nd odi's score")),int(input("enter 3rd odi's score"))) 
# print("you are ",name)
# print("you are achived ",result,"in the last odi series")

if result >=250:
    print("you are selected for next series")
elif result >= 150:
    print("desicion will take on your selection for the next series")
elif result >= 50:
    print("your selection has very low chances")