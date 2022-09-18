import math
while True:
    print('================== mengukur panjang kapal ==================')
    h = float(input('tinggi menara (meter)\t\t\t\t\t: ')) 
    a = float(input('Sudut Elevasi Pengamat Terhadap Ujung Belakang Kapal\t: '))
    b = float(input("Sudut Elevasi Pengamat Terhadap Ujung Depan Kapal\t: "))

    belakang_kapal = h * (math.tan(math.radians(a)))
    depan_kapal = h * (math.tan(math.radians(b)))
    panjang_kapal = belakang_kapal - depan_kapal

    print('=================================================================')
    print("panjang kapal\t\t\t\t\t\t:", round((panjang_kapal), 1), "m")
