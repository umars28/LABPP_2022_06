from re import A


a = input('nilai a:')
b = input('nilai b:')
c = input('nilai c:')

if a > b and a > c :
    print(a,'adalah nilai terbesar')
elif b > a and b > c :
    print(b, 'adalah nilai terbesar')
elif c > a and c > b :
    print(c, 'adalah nilai terbesar')
else:
    print('nilai sama')
