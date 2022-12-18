# Tugas program 2

class BangunRuang:
    def __init__(self, lebar, tinggi, panjang):
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang
    def setTinggi(self, tinggi):
        self.tinggi = tinggi
    def setPanjang(self, panjang):
        self.panjang = panjang
    def setLebar(self, lebar):
        self.lebar = lebar  
    def setMassa(self, massa):
        self.massa = massa
    def getMassaJenis(self):
        return(self.massa/(self.lebar*self.tinggi*self.panjang))

lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

Kubus = BangunRuang(lebar,tinggi,panjang)
Kubus.setMassa(massa)
print("Massa Jenis =", Kubus.getMassaJenis())

Kubus.setMassa(massa * 2)
print("Massa Jenis =", Kubus.getMassaJenis())