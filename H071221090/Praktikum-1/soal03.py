#menghitung volume dan luas permukaan kerucut

print ('---Menghitung Volume  dan Luas Kerucut---')
print ('    -------------------------------------')
print ("Diketahui :")
r = int(input("Jari-jari Kerucut : ")) 
t = int(input("Tinggi Kerucut    :"))

import math
s = math.sqrt(r**2+t**2)

volume = (math.pi*(r**2)*t)/3
area = math.pi*(r**2) + math.pi*r*s

print ("Volume Kerucut adalah         : %0.2f" % area)
print ("Luas Permukaan Kerucut adalah : %0.2f" % volume)