class Weapon(object):
    
    def __init__(self,name = "unidentified weapon", damage = 1, critChance = 1, blockChance = 1, prefix ="" ,suffix = ""):
        self.name = name
        self.damage = damage
        self.critChance = critChance
        self.blockChance = blockChance
        self.prefix = prefix
        self.suffix = suffix
    
    def stats(self):
        print "The Stats of", self.name,"are as follows:"
        print "Damage =",self.damage
        print "Crticial Strike Chance =",self.critChance
        print "Block Chance =",self.blockChance
                
    def prefixGet():
        # prefix to be added: poisoning, burning
        prefixList = ["Sharp","Strange","Bulky","","Damaged"]
        return random.randchoice(prefixList)
        
    def prefixAdd(self):
        pass
        
