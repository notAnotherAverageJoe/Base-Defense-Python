class Zombies:
    def __init__(self,  health):
        self.health = health
        
        
    def attackingBase(self):
        print(f"A zombie swarm moves towards the base - Horde health: {self.health}")
        