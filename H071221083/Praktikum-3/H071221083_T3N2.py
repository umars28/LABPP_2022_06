#soal program 2
#buat perulangan
while True:
 #input degree 
    derajat = float(input("Masukkan besar derajat = "))

#convert degree to time in seconds 
    waktu_detik = 3600 / 15 * derajat  #3600 = many seconds / hour, #15 = 360 in degree / 24 hour 
    #waktu_detik = 3600 / 30 * derajat #statement if 720° or 2 spin

#convert time in seconds to hours:minutes:seconds format
    jam = int(((waktu_detik / 3600) + 6 ) % 24) # +6 = start from 6 A.M., # %24 = limit to 24 Hours,
    menit = int(waktu_detik / 60 % 60 ) # %60 = limit to 60 minutes
    detik = int((waktu_detik % 60)) # %60 = limit to 60 seconds

#print output
    #using if elif to determine time
    if jam >= 5 and jam < 12:
        print ("Selamat pag!")
    elif jam >= 12 and jam < 16:
        print ("Selamat siang!")
    elif jam >= 16 and jam < 18:
        print ("Selamat sore!")
    elif jam >= 118 and jam < 5:
        print ("Selamat malam!")

    print ("{}:{}:{}". format(jam , menit, detik)) 