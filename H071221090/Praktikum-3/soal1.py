x =int(input("Masukkan angka:  "))
y =int(input("Masukkan angka:  "))

if x < y:
    for i in range(1,y+1):
        print(i, end= ' ')
        if i % x == 0:
            print()
else:
    print('inputan tdk valid')