from person import Person
from goblin import Goblin
from weapon import Weapon
'''OOP game
'''



person_1 = Person("Bob",100,10)
person_2 = Person("Chris",1,1)
person_3 = Person("Ryan",999,300)
goblin_1 = Goblin("Gobby",100,10)
weapon_1 = Weapon("Sword",100,3)

print(person_1.get_name())
print(person_2.get_health())
print(person_1.health)


person_1.health = Goblin.goblin_attack(person_1.health)
print(person_1.get_health())

person_1.stamina = Person.power_up(person_1.stamina)
print(person_1.stamina)


# str = 
print(weapon_1.pick_up_weapon())
