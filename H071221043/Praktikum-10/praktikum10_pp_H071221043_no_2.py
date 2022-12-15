#encapsulation
class Burung:
    def __init__(self, jenis):
        self._jenis = jenis
    
    def getJenis(self):
        return self._jenis
      
#inheritance
class Kakatua(Burung):
    def __init__(self, jenis):
        super().__init__(jenis)

    def terbang(self):
        print("Burung Kakatua sedang terbang!")

class Penguin(Burung):
    def __init__(self, jenis):
        super().__init__(jenis)
    
    def terbang(self):
        print("Penguin tak dapat terbang!")

#abstrak
from abc import ABC, abstractmethod
class Elang(ABC):
    @abstractmethod
    
    def terbang(self):
        pass

#polymorphism
def test_terbang(Burung):
    Burung.terbang()

a = Kakatua("Kakatua")
b = Penguin("Penguin")

test_terbang(a)
test_terbang(b)
