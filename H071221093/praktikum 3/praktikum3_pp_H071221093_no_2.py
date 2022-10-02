x = int(input('suku ke:'))

sukuA = 0
sukuB = 1

for i in range(x):
    print(sukuA, end = ' ')
    suku_ke_n = sukuA + sukuB
    sukuA = sukuB
    sukuB = suku_ke_n
    