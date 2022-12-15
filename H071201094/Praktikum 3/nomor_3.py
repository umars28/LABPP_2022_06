bayar = int(input("Bayar barang : "))
harga = int(input("Harga barang : "))

Uang = [100000, 75000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100 ]
kembalian = bayar - harga
print("Kembalian : ", kembalian)

for uang in Uang :
    if uang > kembalian :
        Banyak_Uang = 0
    Banyak_Uang = int(kembalian / uang)
    kembalian = kembalian - (uang * Banyak_Uang)
    print(Banyak_Uang, "Uang Rp. ", uang)