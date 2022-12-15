from pahlawan import Warrior,Support,Assassin
warrior = Warrior("Adit", pos_x=10)
assassin = Assassin("Sopo", pos_x=25)
support = Support("Jarwo", pos_x=30)

#sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)
#sesudah
print("health (after)", warrior.getHealth())

print("-"*10)

#sebelum
print("warrior (health)", warrior.getHealth())
print("support (speed)", support.getSpeed())
support.special(warrior) 

#sesudah
print("warrior (health)", warrior.getHealth())
print("support (speed)", support.getSpeed())
warrior.heal()
print(warrior.getHealth())

