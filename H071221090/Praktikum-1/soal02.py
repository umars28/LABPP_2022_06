#Konversi detik ke dalam format jam;menit:detik

detik = int(input("Masukkan Jumlah Detik yang ingin di Hitung : "))

Jam = detik // 3600;
sisa_detik = detik % 3600;
menit = sisa_detik // 60;
Detik = sisa_detik % 60;

print (Jam,":",menit,":",Detik,":")