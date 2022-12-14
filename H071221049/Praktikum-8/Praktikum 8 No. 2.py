class kubus :
    def __init__ (self, setLebar, setTinggi, setPanjang) :
        self.setLebar = float(setLebar)
        self.setTinggi = float(setTinggi)
        self.setPanjang = float(setPanjang)
    def setMassa (self, setMassa) :
        self.massa = float(setMassa)
    def getMassaJenis(self) :
        return self.massa/(self.setLebar*self.setTinggi*self.setPanjang)

lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

kubus = kubus(lebar, tinggi, panjang)

kubus.setMassa(massa)
print ("Massa Jenis =", kubus.getMassaJenis())

kubus.setMassa(massa*2)
print ("Massa Jenis =", kubus.getMassaJenis())