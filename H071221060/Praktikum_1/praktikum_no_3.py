import math

#variabel
nama_seler = (input('nama seller: '))
gaji_pokok = float(input('gaji pokok: '))
total_penjualan = float(input('total penjualan: '))

total_gaji = ((total_penjualan*15/100)+gaji_pokok)

print("total: %0.2f" %total_gaji)