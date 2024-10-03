from turrets import Turrets
from shield import Shield


class BaseDef(Turrets,Shield):
    def __init__(self, name, health, ammo, power, base_defense,shields,recharge_rate):
        Turrets.__init__(self, health, ammo, power)  # Call the parent class constructor
        Shield.__init__(self, shields, recharge_rate) # Calling second parent constructor
        self.base_defense = base_defense  # Add new attribute for Base
        self.name = name
        
    def base_status(self):
        try:
            print(f"Base Defense Health: {self.base_defense}")
            main_base.shooting()
            main_base.powered()
            main_base.shield_strength()
        except AttributeError as err:
            print(f"issues arose with base status {err}")
        

        
        
main_base = BaseDef("Iron Side", 125, 100, 100, 150, 120, 10)

main_base.base_status()