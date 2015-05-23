import random

class LivingBeing(object):
    def checkForDeath(self):
        if self.health <= 0:
            return True
        return False
    
    def block(self):
        if random.randint(1,100) <= self.weapon.blockChance:
            return True
        return False

    def criticalStrike(self):
        if random.randint(1,100) <= self.weapon.critChance:
            return True
        return False
        
    def attack(self,playerBeingAttacked):
        flagForAttack = False
        while flagForAttack == False:
            if playerBeingAttacked.block() == True:
        	    print self.name + "'s", " Attack was blocked!"
        	    flagForAttack = True
            if self.criticalStrike() == True:
                if flagForAttack == False:
    	            print self.name, "landed a critical strike dealing", self.weapon.damage*2,"damage!"
                    playerBeingAttacked.health -= self.weapon.damage*2
                    print playerBeingAttacked.name, "has", playerBeingAttacked.health, "health remaining!"
                    flagForAttack = True
            else:
                if flagForAttack == False:
                    print self.name, "deals", self.weapon.damage,"damage!"
                    playerBeingAttacked.health -= self.weapon.damage
                    print playerBeingAttacked.name, "has", playerBeingAttacked.health, "health remaining!"
                    flagForAttack = True
            
    def healthRefill(self):
        self.health = 100+(self.level*18)