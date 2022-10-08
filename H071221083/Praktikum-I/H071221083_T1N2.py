#soal program 2
#input seconds
detik = int(input('Input detik: '))

#convert seconds to hours:minutes:seconds format
jam = int(detik / 3600)
menit = int((detik % 3600) / 60)
detik = int((detik % 3600 % 60))

#print output
print("%02d:%02d:%02d" % (jam, menit, detik))