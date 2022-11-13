#soal program 3
#input data
harga = int(input("Masukkan harga barang = Rp. "))
bayar = int(input("Masukkan nilai uang yang dibayarkan = Rp. "))

#make a list 
uang = (100000, 50000, 20000, 10000, 5000, 2000, 1000)
kembalian = bayar - harga

#print output
#using if elif to select the denomination, then print output
if bayar > harga:
    for pecahan in uang: #pecahan= the amount of money in Indoensia, according the question
        jumlah = kembalian // pecahan #jumlah= lots of banknotes
        kembalian -= jumlah * pecahan
        print ("{} uang Rp. {}". format (jumlah, pecahan))
elif bayar < harga:
    print ("Transaksi tidak valid")