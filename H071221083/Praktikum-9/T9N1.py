from Hero import Warrior, Assassin, Support

warrior = Warrior("bambang",pos_x=10)
assassin = Assassin("joko", pos_x=25)
support = Support("udin",pos_x=30)

# sebelum
print("health (before)", warrior.getHealth())

assassin.attack(warrior)

# sesudah
print("health (after)", warrior.getHealth())

print("-"*10)

# sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())

support.setspecial(warrior)

# sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())

# support.move_Setter("L")
# print(f"support posisi = {support.move_Getter()}")
# print(warrior.name)
# print("Before", assassin.getHealth())
# warrior.setSpecial(assassin)
# print("After", assassin.getHealth())
# print(warrior.getArmor(), warrior.getPower())