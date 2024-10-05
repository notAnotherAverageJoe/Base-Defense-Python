from turrets import Turrets
from shield import Shield
from zombie import Zombies
import random as rand
from explorer import Explorer


class BaseDef(Turrets,Shield):
    def __init__(self, name, health, ammo, power, base_defense,
                 shields,recharge_rate, squad_hp, success_rate, carry_capacity,
                 squad_name, squad_level):
        Turrets.__init__(self, health, ammo, power)  # Call the parent class constructor
        Shield.__init__(self, shields, recharge_rate) # Calling second parent constructor
        Explorer.__init__(self, squad_hp, success_rate, carry_capacity, squad_name, squad_level )
        self.base_defense = base_defense  # Add new attribute for Base
        self.name = name
        
    def base_status(self):
        try:
            print(f"Base Defense Health: {self.base_defense}")
            print(f"Turret Ammo: {self.ammo}")
            print(f"Base Shield Strength: {self.shields}")
          
        except AttributeError as err:
            print(f"issues arose with base status {err}")
        

        

def combat_zombie_swarm(zombie, base):
    
    zombie_swarm_hp = zombie.health  # Health of the attacking zombies

    while base.ammo > 0 and zombie_swarm_hp > 0:
        defensive_fire = rand.randint(1, 20)  # This value could represent the damage dealt
        print(f"Zombies are here!\nCurrent Ammo: {base.ammo}\nZombie Swarm Health: {zombie_swarm_hp}")

        # Simulate firing at the zombie swarm
        damage = defensive_fire
        zombie_swarm_hp -= damage  # Reduce the zombie health by the damage dealt
        base.ammo -= 1  # Deduct 1 ammo directly from the base object

        print(f"You fired and dealt {damage} damage to the zombies!")
        print(f"Remaining Zombie Swarm Health: {zombie_swarm_hp}")

        # Check ammo status
        if base.ammo == 0:
            print("No ammo remains.")
            print("Shields will take damage for this.")
            base.shields -= 50  # Reduce shield strength directly from the base
            print(f"Shield Health: {base.shields}")
            break

    if zombie_swarm_hp <= 0:
        print("You survived this wave!")
    else:
        print("The zombies overwhelmed your base!")

        
    
    
