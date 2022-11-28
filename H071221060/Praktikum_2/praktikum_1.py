#konversi nilai dalam  bentuk angka ke huruh

nilai = int(input('Masukkan nilai: '))

if nilai >= 90 and nilai <= 100:
    print("A")
elif nilai >= 80 and nilai <= 89:
    print("B")
elif nilai >= 70 and nilai <= 79:
    print("C")
elif nilai >= 60 and nilai <= 69:
    print("D")
elif nilai >= 40 and nilai <= 59:
    print("E")
elif nilai < 40 and nilai >= 1:
    print("F")
else:
    print("nilai salah")