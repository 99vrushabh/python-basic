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
b = greet(a)