from random import sample


# write method in file
f=open("another.txt","x")
f.write("this is new file")
print(f.read())
f.close()
