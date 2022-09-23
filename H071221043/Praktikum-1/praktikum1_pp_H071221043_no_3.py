#masukkan pemakaian listrik (watt)
listrik_harian = int(input('Input rata-rata pemakaian listrik harian (watt): '))

#pemakaian listrik bulanan (watt)
listrik_bulanan = listrik_harian*30
#Kwh
listrik_bulanan_kwh = listrik_bulanan/1000

#total tagihan 
tagihan = listrik_bulanan_kwh * 1325


print('Tagihan listrik bulanan: Rp.%0.2f' % tagihan)