#program02
#input detik
detik = int(input('detik: '))

#convert detik ke jam : menit : detik
jam = int(detik / 3600)
menit = int((detik % 3600) / 60)
detik = int(detik % 3600 % 60)

#print output
print("%02d : %02d : %02d" % (jam, menit, detik))