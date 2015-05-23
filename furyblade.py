import weapon

class FuryBlade(weapon.Weapon):
    
    def __init__(self,name = "unidentified weapon", damage = 3, blockChance= 0, critChance = 5):
        self.name = name
        self.damage = damage
        self.critChance = critChance
        self.blockChance = blockChance
        