'''Initializing person through a class'''
from unicodedata import name

class Weapon:
    
    def __init__(self,name,durability,damage):
        '''
        Parameters:
            name
                name of weapon
            durability
                durability points
            damage
                damage points
        '''
        self.name = name
        self.durability = durability
        self.damage = damage
    
    def pick_up_weapon(self):
        str = f"You picked up {self.name}. \nDurability = {self.durability} \nDamage = {self.damage}"

        return str
