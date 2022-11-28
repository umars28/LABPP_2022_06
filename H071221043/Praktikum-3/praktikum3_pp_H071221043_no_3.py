harga_barang = int(input('Masukkan harga barang : '))
uang_yang_dibayarkan = int(input('Masukkan nilai uang yang yang dibayarkan :'))

nominal = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

kembalian = uang_yang_dibayarkan - harga_barang
print("Kembaliannya adalah : Rp.", kembalian)

for uang in nominal :
    if uang > kembalian :
        banyak_uang = 0
    banyak_uang = int(kembalian / uang)
    kembalian = kembalian - (uang * banyak_uang)
    print(banyak_uang, 'lembar uang Rp.', uang)