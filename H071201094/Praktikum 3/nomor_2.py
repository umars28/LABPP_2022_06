x = int(input("Suku ke : "))
suku_A = 0
Suku_B = 1

for i in range(x) :
    print(suku_A, end = " ")
    Suku_ke_n = suku_A + Suku_B
    suku_A = Suku_B
    Suku_B = Suku_ke_n