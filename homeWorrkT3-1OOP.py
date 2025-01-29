# Make a function that generates a list of objects with a random class. The classes of objects
# can be Rabbit or Turtle. Both of these classes have a method "run". The method "run"
# randomly generate how many meters the animal crosses in the current minute. The distance
# per minute must be limited by the class of an animal. Make a metaclass that display a
# distance passed by each class of animal each minutes. Make a simulation of the generation
# of a list of random animals that ran for 60 minutes and print results for each animal and
# class.
import random

class Animal:
    def __init__(self, animalType, maxLenInStep):
        self.animalType = animalType
        self.maxLenInStep = maxLenInStep
    
    def run(self) -> int:
        return random.randint(1, self.maxLenInStep)
        
#a = Animal("dog",16)
#print(a.run())
class Rabbit(Animal):
    def __init__(self, petsName):
        self.petsName = petsName
        super().__init__(animalType="Rabbit", maxLenInStep=30)

       
class Turtle(Animal):
    def __init__(self, petsName):
        self.petsName = petsName
        super().__init__(animalType="Turtle", maxLenInStep=10)


def listOfObj(minuteDurations:int):
    turtleList :int  =[]
    rabbitList :int =[]
    for i in range(minuteDurations):
        rabbit = Rabbit(petsName="Brave white")
        turtle = Turtle(petsName="Strong brown")
        rabbitList.append(rabbit.run())
        turtleList.append(turtle.run())
        i +=1
        if i >= minuteDurations:
            break
    return f"{sum(rabbitList)} meters - rabbit it called \"{rabbit.petsName}\", {sum(turtleList)}meters - turtle, it called \"{turtle.petsName}\", the race time was {minuteDurations} minutes"

print(listOfObj(60))
