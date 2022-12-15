a = int(input("masukkan nilai: "))

if a >= 90:
    print("nilai = A")
elif a >= 80 and a < 90:
    print("nilai = B")
elif a >= 70 and a < 80:
    print("nilai = C")
elif a >= 60 and a < 70:
    print("nilai = D")
elif a >= 40 and a < 60:
    print("nilai = E")
elif a < 40:
    print("nilai = F")
else:
    print("masukkan nilai angka")