from re import A
from unicodedata import name


a = input("first number:")
b = input("second number:")
a = int(a)
b = int(b)

print("the value of a+b is", a + b)

# 2
a = 10
b = 4
avg = ((a+b)/2)
print("the value of a+b is", avg)

# string
# 1
a = "hello world's"
print(a)
print(type(a))

# 2
a = 'hello world"s'
print(a)
print(type(a))


# 3
a = ''' world's 
     "world" '''
print(a)
print(type(a))


# concatenating two str.
# greetings ="good morning, "
user="vrushabh"
# c=greetings+user
print(user[2])
print(type(user))

# slicing
print(user[0:3])
# also use as
print(user[:4]) #--> is same as [0:4]
print(user[1:]) #--> is same as [1:last index]
print(user[-4:-2]) #--> is same as [4:6]

# skip value in slice
# in the [third value is skip value]
 
a="vnsguisuni."
print(a)
print(a[0::2])

# string functions
# 1 --> for count numbers of string using =len
story="hello world this is a weather of rain."
print(len(story))

# 2 --> for checking that the var.is end with that word, which is return true or false only =endswith
# formate is print (var.endswith("any word")
print(story.endswith("rain.")) #-->print true
print(story.endswith("hello")) #-->print false

# 3--> for count the number of carrector= count
print(story.count("world"))

# 4--> for make first word capital=capitlize
print(story.capitalize())

#5--> for finding  some word=find
print(story.find("hello"))
print(story.find("winter"))

# 6--> for replace any word =replace
print(story.replace("rain","winter"))


# escap sequnce
# 7(\n,\t,\--for space)
story="hello world this is a weather of rain.\nthis is very\''bad session"
print(story)
