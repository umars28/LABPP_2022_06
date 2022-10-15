#nomor 3

a = int(input('Masukkan nilai a :'))
b = int(input('Masukkan nilai b :'))
c = int(input('Masukkan nilai c :'))

if a > b > c :
    print('Nilai dari bilangan terbesar adalah', a)
elif b > a > c :
    print('Nilai dari bilangan terbesar adalah', b)
else : 
    print('Nilai dari bilangan terbesar adalah', c)