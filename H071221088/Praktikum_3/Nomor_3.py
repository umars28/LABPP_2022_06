a = int(input('Harga barang: '))
b = int(input('Nilai uang yang di bayarkan: '))
kembalian = b-a
uang = (100000,50000,20000,10000,5000,2000,1000)

if a < b:
    for i in uang:
        c = kembalian // i
        kembalian -= c*i
        print(c,'Uang Rp.',i)
elif a == b:
    print('Rp.0')
else:
    print('Nilai yang dibayarkan harus lebih besar dari harga barang')