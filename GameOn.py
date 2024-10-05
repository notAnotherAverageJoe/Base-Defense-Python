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
    print("\n\n1. Check base status")
    print("2. Recharge shields")
    print("3. Send Out Explorers")
    print("4. Exit")
    choices = int(input("Choose an option: \n\n\n"))
    
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
            print("Create a squad of survivors")
            name = input("Choose a name for your Squad! --> ")
            main_squad = Explorer(squad_hp=100,success_rate=50, carry_capacity=50, squad_name=name, squad_level=1)
            main_squad.squad_details()
            
            
        case 4:
            print("Exiting the game. Stay safe!")
            alive = False
        
        case _:
            print("Invalid choice. Please choose again.")

