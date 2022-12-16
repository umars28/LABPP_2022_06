def faktorial(n):
    if n == 0:
        return 1
    else:
        return n*faktorial(n-1)

try:
    n = int(input('Masukkan angka: '))
except:
    print('Inputan harus berupa angka')
else:
    if  n > 0:
        print(n,'! =',faktorial(n))
    else:
        print('Inputan harus berupa angka positif')