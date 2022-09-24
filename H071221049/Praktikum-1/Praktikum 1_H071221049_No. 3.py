#Program03
#import modul
import math 

#input ball diameter
d = int(input('Input diameter bola: '))
r = d/2

#calculate volume
volume = (4/3)*math.pi*(r**3)

#print volume
print('volume bola = %0.2f' % volume)
