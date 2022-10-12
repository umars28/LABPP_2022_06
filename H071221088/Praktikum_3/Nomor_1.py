a = int(input('Masukkan Nilai X: '))
b = int(input('Masukkan Nilai Y: '))

if a < b:
    for i in range(1,b+1):
        print(i, end= ' ')
        if i % a == 0:
            print()
else:
    print('nilai x harus lebih besar dari y')

