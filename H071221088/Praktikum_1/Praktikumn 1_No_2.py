#Nomor 2

detik  = int(input("masukkan detik: "))

jam = detik // 3600;
sisa_detik = detik % 3600;
menit = sisa_detik //60;
detik = sisa_detik % 60;


print("%s : %s : %s" % (jam,menit,detik))