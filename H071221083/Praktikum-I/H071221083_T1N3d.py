#soal program 3
#import math modul
import math

#input ball diamater
d = int(input('Input diameter bola: '))
r = d/2

#calculate volume
volume = (4/3)*math.pi*(r**3)

#print volume
print('Volume bola = %0.2f' % volume)