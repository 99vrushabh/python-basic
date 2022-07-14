# tuple is just like list but main dff. is we can change in list but we cannnot change the value in tuple
tuple=(1,2,3,45,56)


# type of tupple
tuple=() #this is empty tuple
tupple=(1,) #this is single value tupple (, is important)
tupple=(4,5,6) #this is normal tupple

# try to change the value of tupple
# tuple[0]=98
# print(tuple[0])
# error

# tuple methodss
# 1 count
tuple=(1,2,3,45,1,56,1)
print(tuple)
print(tuple.count(1))

# 2 index
print(tuple.index(45))
