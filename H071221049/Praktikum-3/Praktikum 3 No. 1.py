x = int(input("masukkan angka: "))
y = int(input("masukkan angka: "))

if x < y:
    for i in range(1, y+1):
        print(i, end=" ")
        if i % x == 0 :
            print()
else: 
    print('inputan tidak valid')