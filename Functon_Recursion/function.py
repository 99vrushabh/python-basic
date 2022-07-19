def abc(marks):
    result = ((marks[0]+marks[1]+marks[2]+marks[3])/2)
    return result

a=[int(input("enter 1st number")),int(input("enter 2nd number")),int(input("enter 3rd number")),int(input("enter 4th number"))]
form = abc(a)
print(form,"%")
if form >= 80:
    print("congartulation!\nYou Are Passed With A+")
elif form >=70:
    print("Your perfomance is nice,but next time work hard to get much better result")
else:
    print("sorry! you are failed in this year \n Better luck next time ")

def calculate (num1, num2=4):
  res = num1 * num2
  print(res)

calculate(5, 6)