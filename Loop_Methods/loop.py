# while loop
l = 0
while(l < 10):
    print("yes", str(l))
    l = l+1

# print the value 0 to 50
i = 0
while i < 5:
    print("hello")
    i = i+1

# list in while loop
player = ["kohli", "dhoni", "ronaldo", "werner"]
i = 0
while i < len(player):
    print(player[i])
    i = i+1

# FOR LOOP
player = ["kohli", "dhoni", "ronaldo", "werner"]

for item in player:
    print(item)

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