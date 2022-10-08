x = int(input('Masukkan angka x: '))
y = int(input('Masukkan angka y :'))

if x<y :
        for i in range (1, y + 1 ):
                print(i, end=' ') 
                if (i%x == 0):
                        print('\n') 
else :
        print('Data tidak valid')