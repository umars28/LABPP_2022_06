#Import module
import math


#input value of h, a, and b
h = int(input('Input ketinggian menara (h): '))
a = int(input('Input sudut elevasi pengamat terhadap ujung depan kapal (a): '))
b = int(input('Input sudut elevasi pengamat terhadap ujung belakang kapal (b): '))

#convert a and b to radian
tower_to_backOfShip = math.tan(math.radians(a))*h
tower_to_frontOfShip = math.tan(math.radians(b))*h

#calculate length of the ship
length_of_ship = math.sqrt((tower_to_backOfShip - tower_to_frontOfShip)**2)

#print length of ship
print("Panjang kapal =%5.1f m" % length_of_ship)