# making result
maths=int(input("Enter Your Maths Marks :\n"))
science=int(input("Enter Your science Marks :\n"))
gujrati=int(input("Enter Your gujrati Marks :\n"))
ac=int(input("Enter Your ac.Marks :\n"))
total=[maths+science+gujrati+ac]
print("Maths: ",maths)
print("science: ",science)
print("gujrati: ",gujrati)
print("ac: ",ac)
print("total:-",total)

# input using function
def result(marks):
    p=((maths+science)/2)
    return p
mydict={}
maths=int(input("Enter Your Maths Marks :\n"))
science=int(input("Enter Your science Marks :\n"))
life=result(mydict)
print(life)