# for get date and time...
from cmath import sqrt
import datetime
import math
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))


# for give power to one to two..
a=pow(2,3)
print(a)

# for square root
a=math.sqrt(64)
print(a)
import math


# for convert real numbers to int.
x = math.ceil(1.4)
y = math.floor(1.4)

print(x) 
print(y) 
# for get pi's value    
a=math.pi
print(a)

def onefuction():
    a=300
    print(a)
onefuction()

import json

person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}

with open('person.txt', 'w') as json_file:
  json.dump(person_dict, json_file)