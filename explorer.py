class Explorer:
    def __init__(self, squad_hp, success_rate, carry_capacity, squad_name, squad_level):
        self.squad_hp = squad_hp  
        self.success_rate = success_rate  
        self.carry_capacity = carry_capacity  
        self.squad_name = squad_name
        self.squad_level = squad_level
        
    def exploration(self):
        print(f"{self.squad_name} is heading out on an expedition")
        
    def squad_details(self):
        print(f"\n\nSquad name: {self.squad_name}")
        print(f"Squad health: {self.squad_hp}")
        print(f"Success Rate: {self.success_rate}")
        print(f"Carry Capacity: {self.carry_capacity}")
        print(f"Squad Level: {self.squad_level}")
        
