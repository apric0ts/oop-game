'''Initializing person through a class'''
from unicodedata import name

class Goblin:

    def __init__(self,name,health,stamina):
        '''
        Parameters:
            name
                name of person
            health
                hit points
            stamina
                stamina points
        '''
        self.name = name
        self.health = health
        self.stamina = stamina
    
    def goblin_attack(health):
        health-=5
        return health
