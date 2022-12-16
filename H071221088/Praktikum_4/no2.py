def getFPB(x,y):
    if (y==0):
        return x
    else:
        return getFPB(y, x % y)

x = int(input('Masukkan nilai pertama = '))
y = int(input('Masukkan nilai kedua = '))

if x == 0 and y == 0:
    print("Infinity")
else:
    print('FPB dari',x,'dan',y,'=',getFPB(x,y))