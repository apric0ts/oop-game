'''Initializing person through a class'''
from unicodedata import name


class Person:
    #everyone has luck variable
    luck = 999
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

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def power_up(stamina):
        stamina*=1.5
        return stamina