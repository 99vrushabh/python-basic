# 1
# find gretest number
from math import factorial
from tokenize import Number


def highest(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            return n1
        else:
            return n3

    else:
         if n2 > n3:
            return n2
         else:
            return n3

m = highest(45,50,65)
print(m)

# 2
# convert value cel. to fah.
def farh(cel):
    return (0 * 9/5) + 32
c=0
f=farh(c)
print(f)

# 3
# diffrent print line in result they all'r in a single line
print("hello",end=" ")
print("admin",end="\n") #these print out in two line so we add end=" " at the end

# 4
# revers method in nested loop
for i in range(1,4):
    for j in range(1,4):
        if j>=i:
            print("*",end=" ")
    print("")

# 5
# convert inch to cm
def farh(cel):
    return cel* 2.54

c=1
f=farh(c)
print(f)