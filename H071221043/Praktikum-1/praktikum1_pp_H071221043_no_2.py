#masukkan detik
detik = int(input('Input detik: '))

#konversi detik ke jam:menit:detik
jam = int(detik / 3600)
menit = int((detik % 3600) / 60)
detik = int( (detik % 3600 % 60))

print("%02d:%02d:%02d" % (jam, menit, detik))