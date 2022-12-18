class Human:
    def __init__(self, nama, pos_x):
        self.name = nama
        self.__pos_x = pos_x
    def setName(self, nama):
        self.name = nama
    def getName(self):
        return self.name
    def setPosx(self, posx):
        self.__pos_x = posx
    def getPosx(self):
        return self.__pos_x
    def move_Setter(self, arah):
        if arah == "L": self.__pos_x -= self._speed 
        elif arah == "R": self.__pos_x += self._speed
    def move_Getter(self):
        return self.__pos_x

class Hero(Human):
    def __init__(self,nama, pos_x):
        super().__init__(nama, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
    def attack(self, target):
        target._health -= self._power
    def setPower(self, pwr):
        self._power = pwr
    def getPower(self):
        return self._power
    def setHealth(self, hlt):
        self._health = hlt
    def getHealth(self):
        return self._health
    def setArmor(self, arm):
        self._armor = arm
    def getArmor(self):
        return self._armor
    def setSpeed(self, spd):
        self._speed = spd
    def getSpeed(self):
        return self._speed     
    
class Warrior(Hero):
    def __init__(self,nama, pos_x):
        super().__init__(nama, pos_x)
        self._armor = 30
        self._power = 26   
    def setSpecial(self, target):
        self._armor = 45
        self._power = 32
        self.attack(target)

class Assassin(Hero):
    def __init__(self,nama, pos_x):
        super().__init__(nama, pos_x)
        self.armor = 4
        self._power = 35
    def setSpecial(self,target):
        self._speed = 7
        self._power = 42
        self.attack(target)

class Support(Hero):
    def __init__(self,nama, pos_x):
        super().__init__(nama, pos_x)
        self._armor = 8
        self._speed = 4
        self._health = 500
    def setspecial(self, target):
        self._speed = 6
        target._health += 150