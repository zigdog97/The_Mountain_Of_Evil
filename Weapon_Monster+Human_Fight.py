import random
class Weapon(object):
    
    def __init__(self,name = "unidentified weapon", damage = 1, critChance = 1, blockChance = 1):
        self.name = name
        self.damage = damage
        self.critChance = critChance
        self.blockChance = blockChance

class Shield(Weapon):
    
    def __init__(self,name = "unidentified weapon", damage = 1, blockChance= 5, critChance = 0):
        self.name = name
        self.damage = damage
        self.critChance = critChance
        self.blockChance = blockChance

godShield = Shield("GOD SHIELD",10000,100,100)
fist = Weapon("fist") 
woodShield = Shield("wooden shield")
    
class LivingBeing(object):
    
    def block(self):
        if random.randint(1,100) <= self.weapon.blockChance:
            return True
        return False

    def criticalStrike(self):
        if random.randint(1,100) <= self.weapon.critChance:
            return True
        return False
        
    def attack(self,playerBeingAttacked):
        if playerBeingAttacked.block() == True:
            print self.name + "'s", " Attack was blocked!"
            pass
        if self.criticalStrike() == True:
    	    print self.name, "landed a critical strike dealing", self.weapon.damage*2,"damage!"
            playerBeingAttacked.health -= self.weapon.damage*2
            print playerBeingAttacked.name, "has", playerBeingAttacked.health, "health remaining!"
        else:
            print self.name, "deals", self.weapon.damage,"damage!"
            playerBeingAttacked.health -= self.weapon.damage
            print playerBeingAttacked.name, "has", playerBeingAttacked.health, "health remaining!"

class Monster(LivingBeing):
    
    def __init__(self,name = "monster", weapon = fist, health = 10, ):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.experienceGive = self.health * 10
        
blendo = Monster("Blendo")

        
class Human(LivingBeing):
    
    def __init__(self,name = "adventurer", weapon = fist, health =100, experienceTotal = 0):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.experienceTotal = experienceTotal
        
zach = Human("Zach",woodShield)
godShieldZach = Human("Zach", godShield) 

