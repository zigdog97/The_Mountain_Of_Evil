import weapon

class Shield(weapon.Weapon):
    
    def __init__(self,name = "unidentified weapon", damage = 1, blockChance= 5, critChance = 0):
        self.name = name
        self.damage = damage
        self.critChance = critChance
        self.blockChance = blockChance