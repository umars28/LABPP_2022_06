class kubus:
    def __init__(self, lebar, tinggi, panjang = 5.0):
        self.lebar = float(lebar)
        self.tinggi = float(tinggi)
        self.panjang = float(panjang)
        
    def setMassa (self, setMassa):
        self.massa = float(setMassa)
    def getMassaJenis(self):
        return self.massa/(self.panjang*self.lebar*self.tinggi)

lebar = float(input('masukkan lebar:'))
tinggi = float(input('masukkan tinggi:'))
panjang = float(input('masukkan panjang:'))
massa = float(input('masukkan massa:'))

objKubus = kubus(lebar, tinggi, panjang)

objKubus.setMassa(massa)
print("massa jenis = ", objKubus.getMassaJenis())
objKubus.setMassa(massa*2)
print("massa jenis = ", objKubus.getMassaJenis())

        