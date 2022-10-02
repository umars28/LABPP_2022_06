
print('masukkan nilai x dan y (x < y)')
x = int(input('nilai x:'))
y = int(input('nilai y:'))

if x < y :
    for i in range(1, y  + 1) :
        print(i, end = ' ')
        if i % x == 0 :
                print()
else :
    print('y harus lebih besar dari x')
