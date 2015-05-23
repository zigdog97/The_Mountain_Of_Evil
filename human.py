import livingbeing, weapon

fist = weapon.Weapon("fist")

class Human(livingbeing.LivingBeing):
    def __init__(self,name = "Stranger", weapon = fist, health =90, experienceTotal = 0, level = 1):
        self.name = name
        self.weapon = weapon
        self.health = health + (level*10)
        self.experienceTotal = experienceTotal
        self.level = level
        
    def levelUP(self):
        self.level +=1
        self.healthRefill()
        
    def checkForLevelUp(self):
        if self.experinceTotal*self.level*.60 >= self.experienceTotal:
            return True
        return False