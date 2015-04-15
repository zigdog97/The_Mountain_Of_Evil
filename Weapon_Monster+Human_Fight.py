import random
class Weapon(object):
    
    def __init__(self, damage = 1, critChance = 1, blockChance = 1):
        self.damage = damage
        self.critChance = critChance
        self.blockChance = blockChance
        
    def block(self):
        if random.randint(1,100) <= self.blockChance:
            return True
        return False

    def criticalStrike(self):
        if random.randint(1,100) <= self.critChance:
            return True
        return False

class Shield(Weapon):
    
    def __init__(self, damage = 1, blockChance= 10, critChance = 5):
        self.damage = damage
        self.critChance = critChance
        self.blockChance = blockChance

fist = Weapon() 
    

class Monster(object):
    
    def __init__(self,name = "monster", weapon = fist, health = 10, ):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.experienceGive = self.health * 10
        
blendo = Monster("Blendo")

        
class Human(object):
    
    def __init__(self,name = "adventurer", weapon = fist, health =100, experienceTotal = 0):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.experienceTotal = experienceTotal
        
zach = Human("Zach")

def attack(playerAttacking,playerBeingAttacked):
    if playerBeingAttacked.weapon.block() == True:
        print playerAttacking.name + "'s", " Attack was blocked!"
        pass
    if playerAttacking.weapon.criticalStrike() == True:
        print playerAttacking.name, "landed a critical strike dealing", playerAttacking.weapon.damage*2,"damage!"
        playerBeingAttacked.health -= playerAttacking.weapon.damage*2
        print playerBeingAttacked.name, "has", playerBeingAttacked.health, "health remaining!"
    else:
        print playerAttacking.name, "deals", playerAttacking.weapon.damage,"damage!"
        playerBeingAttacked.health -= playerAttacking.weapon.damage
        print playerBeingAttacked.name, "has", playerBeingAttacked.health, "health remaining!"