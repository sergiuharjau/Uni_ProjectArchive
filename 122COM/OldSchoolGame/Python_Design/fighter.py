from player import Player,random


class Fighter(Player):

    def __init__(self, name):
        Player.__init__(self,name)
        self.baseDMG += 10
        self.armor += 5
        self.hp += 25
        self.chargingAttack = True
        self.timer = 2
            # START WITH A SWORD

# simple attack deals 25 dmg
# crit strike deals 50 dmg
# power attack deals 70 dmg
# exp attack deals 10-30 dmg
    #if you kill the enemy, gain 25XP

    def powerAttack(self,other):
        if self.timer > 0:
            self.chargingAttack = False
            if self.timer == 2:
                print(str(self.timer) + " turns to charge up.")
            else:
                print(str(self.timer) + " turn to charge up.")
            self.timer -= 1
            
            return
        else:
            self.chargingAttack = True
            self.timer = 2
            print("You smacked him in the head real hard.")
            other.takeDamage(70)

    def expAttack(self, other):
        damage = random.randint(5,35)
        other.takeDamage(damage)
        if other.hp <= 0:
            self.gainEXP(25)
            #extra gold as well once we have it 
