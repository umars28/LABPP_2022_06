#encapsulation
class Fruit:
    def __init__(self, jenis, rasa):
        self._jenis = jenis
        self._rasa = rasa

    def getJenis(self):
        return self._jenis
      
    def getRasa(self):
        return self._rasa
#inheritance
class Anggur(Fruit):
    def __init__(self, jenis, rasa):
        super().__init__(jenis, rasa)

    def membandingkan(self, target):
        print("buah Anggur lebih manis daripada buah " + target.getJenis())

class Semangka(Fruit):
    def __init__(self, jenis, rasa):
        super().__init__(jenis, rasa)

    def membandingkan(self, target):
        print("buah semangka lebih segar daripada buah " + target.getJenis())
        
# #interface
# def membandingkan(Fruit):
#     Fruit.rasa()

#class abstrak
from abc import ABC, abstractmethod
class Durian(ABC):
    @abstractmethod
    def rasa(self):
        pass

#objek
a = Anggur("Anggur", 'manis')
b = Semangka("Semangka", 'kurang manis')

#interface (polymorphism)
b.membandingkan(a)
a.membandingkan(b)