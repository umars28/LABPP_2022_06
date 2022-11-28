bayar = int(input('bayaran anda:'))
harga = int(input('harga barang:'))

JenisUang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100 ]
kembalian = bayar - harga
print('kembalian:', kembalian)

for uang in JenisUang:
    if uang > kembalian :
        BanyaknyaUang = 0
    BanyaknyaUang = int(kembalian / uang)
    kembalian = kembalian - (uang * BanyaknyaUang)
    print(BanyaknyaUang, 'uang Rp.', uang) 
