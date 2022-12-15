a = int(input('Masukkan nilai a: '))
b = int(input('Masukkan nilai b: '))
c = int(input('Masukkan nilai c: '))

if a > b and a > c:
    print(str(a) + ' adalah nilai terbesar')
elif b > a and b > c:
    print(str(b) + ' adalah nilai terbesar')
else:
    print(str(c) + ' adalah nilai terbesar')