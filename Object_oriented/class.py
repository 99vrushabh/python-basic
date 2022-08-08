from email.mime import application
from time import time
# this is data for indivitiual var.

class cars:
    carsType = "all_in_the_world"
    def carsData(self):
        print(f"that was {self.name} car")
        print(f"that was published in the year of {self.year} ")
CarsApplication = cars()
CarsApplication.name=input("Enter your fav. car's name")
CarsApplication.year="1993"
CarsApplication.carsData()


# class
class score:
    # class attribute
    scoreType ="Cricket_match"
    # instance attribute
    def match_score(match):
        print(f"in the first odi india's score was :-  {match.score1}" , f" and in the same match England's score was :-  {match.score2}")
# object instantiantion
ScoreCard = score()
ScoreCard.score1=int(input("Enter India's Score :- "))
ScoreCard.score2=int(input("Enter England's Score :- "))
# accessing class
ScoreCard.match_score()

ScoreDef=ScoreCard.score1-ScoreCard.score2
print(ScoreDef)
if ScoreCard.score1>ScoreCard.score2:
    print("India Won The Match By ",ScoreDef,"runs")
else:
    print("England Won The Match By ",ScoreDef,"runs")

class user:
    userType = "primeUsers"
    def userdata(prime):
        print(f"User's Name :- {prime.name}")
userDetails = user()
userDetails.name="vrushabh"
userDetails.userdata()