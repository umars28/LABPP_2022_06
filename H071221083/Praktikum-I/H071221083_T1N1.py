#soal program 1
#Import math module
import math

#input value of h, a, and b
h = int(input(' ketinggian menara dalam meter(h): '))
a = int(input(' sudut pengamat terhadap ujung depan kapal (a): '))
b = int(input(' sudut pengamat terhadap ujung belakang kapal (b): '))

#convert a and b to radian
menara_belakangkapal = math.tan(math.radians(a))*h
menara_depankapal = math.tan(math.radians(b))*h

#calculate length of the ship
panjang_kapal = math.sqrt((menara_belakangkapal - menara_depankapal)**2)

#print length of ship
print("Panjang kapal =%5.1f m" % panjang_kapal)