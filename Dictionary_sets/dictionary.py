from turtle import update


myDict = {
    "fast": "in a quick manner",
    "mugenta" :"it's a color",
    "numbers" :[1,5,6],
    "other" : {"harry":"potter"}
}
print(myDict["fast"]
# print(myDict["numbers"])
myDict["numbers"]=1239
print(myDict["numbers"])

print(myDict["other"]["harry"])

# dic. methods
# 1 keys
print(myDict.keys())

# 2 values
print(myDict.values())
# 3 items
print(myDict.items())
# 4 update
updatedict ={
   " high" :"which value at a large scale"
}
myDict.update(updatedict)
print(myDict)
# print(myDict.get("dance"))
# print(myDict["dance"])


# ps 
# 1
favlan={}
a=input("enter your fav lan. ronaldo\n")
b=input("enter your fav lan. wright\n")
c=input("enter your fav lan. werner\n")
d=input("enter your fav lan. foden\n")
favlan['ronaldo']=a
favlan['wright']=b
favlan['ronaldo']=c
favlan['foden']=d

print(favlan)
