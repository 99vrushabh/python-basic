# start method
print("this is 1st method")
for i in range(1,5):
    for j in range(1,5):
        if j<=i:
            print("*" , end='')
    print()
# 1st star method in revers
print("this is revers of 1st method")

for i in range(1,5):
    for j in range(1,5):
        if j>=i:
            print("*" , end='')
    print()
 

print("this is 2nd method is star at right side")
for i in range(1,5):
    for k in range(1,5-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*" , end='') 
    print("\n")


print("this is revers of 2st method")
for i in range(5,0,-1):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*" , end='') 
    print("\n")
 

print("this is 3rd method is pyramid")
for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,(2*i-1 )+1):
        print("*" , end='') 
    print("\n")

print("this is revers of 3rd method")
for i in range(5,0,-1):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,(2*i-1 )+1):
        print("*" , end='') 
    print("\n")