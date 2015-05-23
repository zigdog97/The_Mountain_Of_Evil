import livingbeing, weapon

fist = weapon.Weapon("fist")

class Monster(livingbeing.LivingBeing):
    
    def __init__(self,name = "Odd Creature", weapon = fist, health = 10, ):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.experienceGive = self.health * 10