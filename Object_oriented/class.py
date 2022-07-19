from email.mime import application

class form:
    formType ="SubmittionForm"
    def printData(self):
        print(f"name is {self.name}")
        print(f"train is {self.train}")

formApplication = form()
formApplication.name = "hello22"
formApplication.train = "abc008902 express"
formApplication.printData()
var= "James Bond"
print(var[2::-1])