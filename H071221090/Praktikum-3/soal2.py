derajat = float(input('derajat:  '))
hari = 3600 * 24
detik = round((derajat/360)*hari)
jam = 6
menit = 0

while(detik >=  3600):
    detik -=  3600
    jam += 1

while(detik >= 60):
    detik -= 60
    menit += 1

jam %= 24 

if jam >= 6 and jam < 12:
    print("Selamat pagi")
elif jam >= 12 and jam <= 15:
    print("Selamat siang")
elif jam > 15 and jam <= 18:
    print("Selamat sore")
elif jam > 18 and jam <= 24:
    print("Selamat malam")
else :
    print("Selamat malam")

print('%02d : %02d : %02d '%(jam, menit, detik))
print()