derajat = float(input('derajat: '))
hari = 3600 * 24 #detik * jam
detik = round((derajat/360)*hari)
jam = 6
menit = 0

while(detik >= 3600):
    detik -= 3600 #detik = detik - 3600
    jam += 1 #jam = jam + 1

while(detik >= 60):
    detik -= 60
    menit += 1

jam %= 24 #jam = jam % 24

if jam >= 6 and jam < 12:
    print("selamat pagi")
elif jam >= 12 and jam <= 15:
    print("selamat siang")
elif jam > 15 and jam <= 18:
    print("selamat sore")
elif jam > 18 and jam <= 24:
    print("selamat malam")
else :
    print("selamat malam")

print(f"{jam:02d}:{menit:02d}:{detik:02d}")
