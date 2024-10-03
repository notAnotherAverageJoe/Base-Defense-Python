class Turrets:
    def __init__(self,health,ammo,power):
        self.health = health
        self.ammo = ammo
        self.power = power
        
    def shooting(self):
        print(f"Turret health: {self.health}, Turret Ammo: {self.ammo} ")
        
    def powered(self):
        print(f"Turret power level: {self.power}")
        
        

        
        