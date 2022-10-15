#Import module
import math


#masukkan nilai h, a, and b
h = int(input('Input ketinggian menara (h): '))
a = int(input('Input sudut elevasi pengamat terhadap ujung belakang kapal (a): '))
b = int(input('Input sudut elevasi pengamat terhadap ujung depan kapal (b): '))

#konversi a dan b ke radian
menara_ke_ujung_belakang_kapal = math.tan(math.radians(a))*h
menara_ke_ujung_depan_kapal = math.tan(math.radians(b))*h

#menghitung panjang kapal
panjang_kapal = math.sqrt((menara_ke_ujung_belakang_kapal - menara_ke_ujung_depan_kapal)**2)


print("Panjang kapal =%5.1f m" % panjang_kapal)