import random 

class Elevator():
    
    def __init__(self):
        self.peopleOnElevator = 0 
        self.Level = 0
        
    def enterElevator(self):
        self.peopleOnElevator += 1         
    def exitElevator(self):
        self.peopleOnElevator -= 1 
        
    def goTo(self, level):
        Elevator.movingSequence(self, level)
    def movingSequence(self, destination):
        self.Level = destination 
        #
        #
        #
       
    def getPeople(self):
        return(self.peopleOnElevator)
    def getLevel(self):
        return(str(self.Level))
        
class Person():
    
    def __init__(self,startingLevel):
        self.Level = startingLevel
        self.onElevator = False
        
    def callElevator(self, other):
        if self.Level == other.Level: 
            print("Elevator already here.")
            return
        Elevator.goTo(other, self.Level)
        
    def boardElevator(self, other): 
        if self.Level != other.Level:
            print("No elevator.")
            return
        Elevator.enterElevator(other)
        self.onElevator = True                  
        
    def pressButton(self, other, button):
        if self.onElevator != True:
            print("Nothing to press.")
            return
        if button == self.Level:
            print("Destination reached.")
            return
        Elevator.goTo(other, button)
        self.Level = button 
    
    def exitElevator(self, other):
        Elevator.exitElevator(other)
        self.onElevator = False 
    
    def getStatus(self):
        return("Level: " + str(self.Level) + "\nStatus: " + str(self.onElevator))

E= Elevator()
Sergiu = Person(1)

print(E.getLevel())
print(Sergiu.getStatus())

Sergiu.callElevator(E)
print(E.getLevel())

Sergiu.callElevator(E)


