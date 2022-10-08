#program01
#import module
import math

#input value of h, a,b 
h = int(input('input ketinggian menara (h): '))
a = int(input('input sudut elevasi pengamat terhadap ujung depan kapal (a): '))
b = int(input('input sudut elevasi pengamat terhadap ujung belakang kapal (b): '))

#convert a and b to radian
menara_ke_belakang_kapal = math.tan(math.radians(a))*h
menara_ke_depan_kapal = math.tan(math.radians(b))*h

#calculate panjang kapal
panjang_kapal = math.sqrt((menara_ke_belakang_kapal - menara_ke_depan_kapal)**2)

#print panjang kapal
print("panjang kapal =%5.1f m" % panjang_kapal)