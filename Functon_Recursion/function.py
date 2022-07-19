from unicodedata import name


def abc(marks):
    result = (((marks[0]+marks[1]+marks[2]+marks[3])/200)*100)
    return result

a=[50,45,70,60]
form = abc(a)
print(form,"%")
if form >= 80:
    print("congartulation!\nYou Are Passed With A+")
elif form >=70:
    print("Your perfomance is nice,but next time work hard to get much better result")
else:
    print("sorry! you are failed in this year \n Better luck next time ")

def peoples(firstname,lastname):
    name=firstname + lastname
    return name

lbw=peoples("hello ","world")
print (lbw)