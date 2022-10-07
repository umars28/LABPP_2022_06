#soal program 1
while True:
 #input X & Y
    X = int(input('X = '))
    Y = int(input('Y = '))

#print output
    #using if & for loop to 
    if X < Y:
        for a in range (1, Y + 1):
            print (a, end=' ')
            if a % X == 0:
                print ()