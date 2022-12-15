from abc import ABC, abstractmethod

#class abstract
class Animal(ABC):
    @abstractmethod
    def suara(self):
        pass
#polymorphism
    def __init__(self, nama):
        self.nama = nama

#Inharitance Hewan(Animal)
class Hewan(Animal):
    def __init__(self, nama):
        super().__init__(nama)
        #Encapsulation (_)
        self._suara = "Suara"
    
    #Polymorphism
    def serang(self,target):
        #Encapsulation (_)
        target._health -= self._power
    #Polymorphism
    def bergerak(self):
        print("Bergerak dengan cara")
    #Polymorphism
    def bertarung(self):
        print("Bertarung dengan")

#Inharitance
class ular(Hewan):
    def __init__(self, nama):
        super().__init__(nama)
        #Encapsulation (_)
        self._health = 500
        #Encapsulation (_)
        self._power = 200
    #Polymorphism
    def cekDarah(self):
        #Encapsulation (_)
        print(self._health)
    #Polymorphism
    def serang(self,target):
        #Encapsulation (_)
        target._health -= self._power
    #Polymorphism
    def bergerak(self):
        print("Ular bergerak dengan menggunakan badannya")
    #Polymorphism
    def bertarung(self):
        print("Ular bertarung dengan menggigit musuhnya")
    #Polymorphism
    def suara(self):
        print("sssttttt")
#Inharitance    
class tokek(Hewan):
    def __init__(self, nama):
        super().__init__(nama)
        #Encapsulation (_)
        self._health = 200
        #Encapsulation (_)
        self._power = 75
    #Polymorphism
    def cekDarah(self):
        #Encapsulation (_)
        print(self._health)    
    #Polymorphism
    def serang(self,target):
        #Encapsulation (_)
        target._health -= self._power
    #Polymorphism
    def bergerak(self):
        print("Tokek bergerak dengan menggunakan kaki dan tangannya")
    #Polymorphism
    def bertarung(self):
        print("Tokek bertarung dengan mengigit musuhnya")
    #Polymorphism
    def suara(self):
        print("tokke-tokke")