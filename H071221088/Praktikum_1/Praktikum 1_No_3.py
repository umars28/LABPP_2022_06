#Nomor 3

import math


t = int(input('Masukkan tinggi: '))
r = int(input('Masukkan jari-jari: '))

pelukis = math.sqrt(r**2 + t**2)
luas = (math.pi*r*(r+pelukis))
volume = (math.pi*(r**2)*t)/3

print('Luas Kerucut: %0.2f' % luas)
print('Volume Kerucut: %0.2f' % volume)