# start method
from itertools import count


print("1st method")
for i in range(1, 5):
    for j in range(1, 5):
        if j <= i:
            print("|", end='-')
    print()
# 1st star method in revers
print("revers of 1st method")
for i in range(1, 5):
    for j in range(1, 5):
        if j >= i:
             print("|", end='-')
    print()


print("2nd method is star at right side")
for i in range(1, 5):
    for k in range(1, 5-i):
        print(" ", end="")
    for j in range(1, i+1):
         print("|", end='')
    print("\n")


print("revers of 2st method")
for i in range(5, 0, -1):
    for k in range(1, 6-i):
        print(" ", end="")
    for j in range(1, i+1):
         print("|", end='')
    print("\n")


print("3rd method is pyramid")
for i in range(1, 6):
    for k in range(1, 6-i):
        print(" ", end="")
    for j in range(1, (2*i-1)+1):
        print("-", end='')
    print("\n")

print("revers of 3rd method")
for i in range(5, 0, -1):
    for k in range(1, 6-i):
        print(" ", end="")
    for j in range(1, (2*i-1)+1):
        print("*", end='')
    print("\n")

print("4th method is daimond")
for i in range(1, 6):
    for k in range(1, 6-i):
        print(" ", end="")
    for j in range(1, (2*i-1)+1):
        print("-", end='')
    print("\n")
for i in range(5, 0, -1):
    for k in range(1, 6-i):
        print(" ", end="")
    for r in range(1, (2*i-1)+1):
        print("-", end='')
    print("\n")

print("5th method is left side pyramid")
for i in range(0, 6):
    for j in range(0, i + 1):
        print("* ", end='')
    print("\n")
for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("- ", end='')
    print("\n")

# for multiplication table for many numbers
for i in range(1, 11):
    for j in range(1, 11):
        print(j*i, end="")
    print(" ")

# inner loop and outer loop in nested loop
abc = ["hello", "world", "admin"]
# outer loop
for name in abc:
    # inner loop
    count = 0
    while count < 5:
        print(name, end=" ")
        count = count+1
        print("\n")
# rectangle star
for i in range(1,6):
    for j in range(1,4):
        if j+i:
            print("*",end=' ')
    print() 
    

for i in range(5):
    for j in range(5):
        if i == 5 // 2:
            print('------', end='')
        else:
            if j == 5 // 2:
                print('|', end='')
            else:
                print(' ', end='')
    print()




