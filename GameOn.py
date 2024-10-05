import random as rand
from base_def import BaseDef, combat_zombie_swarm
from zombie import Zombies
from explorer import Explorer


# Initialize the game state
alive = True

def check_for_zombie_spawn():
    zombie_swarm = Zombies(100)
    spawn_zombies= rand.randint(1,10)
    if spawn_zombies % 2 == 0:
        zombie_swarm.attacking_base()
        combat_zombie_swarm(zombie_swarm, main_base)
    else:
        print("No zombies around! You are safe for now...")
        

# Get the base name from the user
base_name = input("Enter a name for your base: ")
main_base = BaseDef(name=base_name, health=125, ammo=100, power=100, base_defense=150, shields=120, recharge_rate=10)

while alive:
    print("\nPrepare for the next attack")
    choices = int(input("\n\n1. Check base status\n2. Recharge shields\n3. Exit\nChoose an option: \n\n\n"))
    
    match choices:
        case 1:
            # Call base status method to show current status
            main_base.base_status()
            check_for_zombie_spawn()
        
        case 2:
            # Recharge the shields
            main_base.recharging() 
            print(f"{main_base.name}'s shields have been recharged!")
            check_for_zombie_spawn()
            
            
        case 3:
            print("Exiting the game. Stay safe!")
            alive = False
        
        case _:
            print("Invalid choice. Please choose again.")

