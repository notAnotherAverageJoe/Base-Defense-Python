class Shield:
    def __init__(self, shields, recharge_rate):
        self.shields = shields
        self.recharge_rate = recharge_rate
        
        
    def shield_strength(self):
        print(f"Shield strength: {self.shields}")
        
    def recharging(self):
        print("Shields are currently recharging!")