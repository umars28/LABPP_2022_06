a = (float(input('Masukkan Nilai Derajat: ')))
c = 240*a

jam = (c//3600) + 6
sisa = c % 3600 
menit = sisa //60
detik = sisa % 60

if a < 270:
    if 6 <= jam < 12:
         print('Selamat pagi')
    elif 12 <= jam < 15:
        print('Selamat Siang')
    elif 15 <= jam < 18:
            print('selamat sore')
elif a > 270 and a <= 360:             
    jam = jam - 24
    if 6 >= jam :
        print('Selamat malam')

print('%02d:%02d:%02d'%(jam,menit,detik))

