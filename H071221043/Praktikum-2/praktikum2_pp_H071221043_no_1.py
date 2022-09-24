n = int(input('Masukkan nilai : '))

if n >= 90 :
    print('Nilai', n, '= A')
elif n >= 80 and n <= 90 :
    print('Nilai', n, '= B')
elif n >= 70 and n <= 80 :
    print('Nilai', n, '= C')
elif n >= 60 and n <= 70 :
    print('Nilai', n, '= D')
elif n >= 40 and n <= 60 :
    print('Nilai', n, '= E')
elif n < 40 :
    print('Nilai', n, '= F')
else :
    print('Data tidak valid')