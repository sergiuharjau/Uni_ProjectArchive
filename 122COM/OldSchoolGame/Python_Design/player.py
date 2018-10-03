# TO DO:
# add backpack (limit itemslist in a way)
# DONE: add base damage
# add actual classes (Start with Fighter)
# DONE: add "attack" function
# DONE: add armor (think about how armor affects damage)
# DONE: add "defend" function, reinforces armor (?)
# DONE: add documentation ( On second thought, not needed )

import time, random

class Player:

    def __init__(self, name):
        self.name = name[0].upper() + name[1:].lower()  #Makes sure it's in the right format
        self.baseDMG = 15  #normal attack damage
        self.armor = 10
        self.tempArmor = 0
        self.level = 1
        self.itemsList = []
        self.hp = 100
        self.hpMAX = 100  #added hpMAX, fixed logic error
        self.experience = 0
        self.expNeeded = 100


    def attack(self, other):
        rng = random.randint(0,2)
        crit = random.randint(0,4)
        if crit == 0:   #1 in 5 chance to crit strike
            print("Critical strike!")
            other.takeDamage(self.baseDMG * 2)
        elif rng in [1,2]: #2 in 3 chance to hit
            print("Normal damage!")
            other.takeDamage(self.baseDMG)
        else:   #1 in 3 chance to miss
            print("Missed!")

    def defend(self):
        rng = random.randint(0,3)
        if rng == 0:  #1 in 4 chance you get double temp armor
            print("Super Defend!")
            self.tempArmor = 20
        else:
            print("Normal armor.")
            self.tempArmor = 10

    def gainEXP(self, experience):
        self.experience += experience
        if self.experience >= self.expNeeded:
            self.levelUP()

    def levelUP(self):
        self.experience -= self.expNeeded  #extra exp carries over
        self.expNeeded = 100 + 10 * 2 * (self.level)  #NOTE: do not place this line after self.level+=1
                 #120xp for level 2, 140xp for level 3, 160xp for level 4, and so on
        self.level += 1
        self.armor += 5
        self.baseDMG += 10
        self.hpMAX += 25     #gain 25 HP per level increase. Level 4 is 200 hp.
        self.hp = self.hpMAX

    def pickItem(self, item):
        self.itemsList.append(item)
            #integrate with Rokas somehow

    def dropItem(self, item):
        if item in self.itemsList:
            self.itemsList.remove(item)
        else:
            print("Nothing to drop.")
                #prefereably configure it so it returns instead of printing
                #also, integrate with Rokas

    def healUP(self, health):
        self.hp += health
        if self.hp > self.hpMAX:  #can't overheal atm
            self.hp = self.hpMAX

    def takeDamage(self, damage):
        self.hp -= damage * ((100 - (self.armor + self.tempArmor)*2)/100) #NOTE: 50 armor would give 100% reduction
        self.tempArmor = 0 #temp armor only shields 1 hit.

        if self.hp <= 0:
            self.death()    #maybe look into making it percentage based reduction

    def death(self):
        print("You have died. Game over.")
        #
        #   Code that makes the game stop
        #


    def giveBrief(self):
        print("Name: " + self.name)
        print("Items: " + str(self.itemsList))
        print("Experience: " + str(self.experience))
        print("Level: " + str(self.level))
        print("HP: " + str(self.hp))




def mainTests():   #uncomment function call to test things out
    p = Player("sERGiu")
    e = Player("Enemy")
    while True:
        p.giveBrief()
        e.giveBrief()
        input("")
        p.attack(e)

#mainTests()