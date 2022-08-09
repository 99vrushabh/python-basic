from calendar import c
from os import scandir
from re import A


s1={1,2,3,4,5,6}
s2={4,5}
s3={8,9}


# for display all dict
print("s1 is :",s1,"\ns2 is :",s2,"\ns3 is :",s3)
# this is math method of intersection
# it means in dict a and dict b have same elements
s4=(s1.intersection(s2))
print("s1 intersectin of s2 is : ",s4)

# this is math method of union
# it means in dict a and dict b have all the  elements in new dict
s5=(s1.union(s2))
print("s1 Union s2 is : ",s5)

# update exist dict 
s1.update([10,11])
print ("updated dict s1 is",s1)                               


# remove some elements from dict 
s1.remove(3)
print("after element(3) remove , new dict s1 is",s1)

# for diffrence betwen two dict
s5 =s1.difference(s2)
print ("diffrence between s1 and s2",s5 )
print("diffrence between s1 and s2",s1.symmetric_difference(s2))

s6=s1.intersection(s2).union(s3)
print(s6)


# math method like subset or superset
s7=s2.issubset(s1)
print(s7)
s8=s1.issuperset(s2)
print(s8)

# for get avg of two numbers
a=int(input("enter a : "))
b=int(input("enter b : "))
c=(a+b)/2

print("a is :",a)
print("b is :",b)
print("c is :",c)

def findItem(e, l):
    for i, el in enumerate(l):
        if el == e:
            return [i, el]
    
    return findItem
# It is possible to print a generator as a list, but you will loose performance
# In a large set of data generators excel in time efficiency
# print(list(myGen))