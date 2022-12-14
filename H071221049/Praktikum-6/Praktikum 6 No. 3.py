filename = input() + ".txt"
satu = int(input())

baru = open(filename, "w+")

try:
    baru.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")
    baru.write("|" + " Nama" + " "*17 + "|" + " NIM" + " "*8 + "|" + " Angkatan" + " " + "|" + "\n")
    baru.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")

    for i in range(satu):
        nama = input().replace(" ","_")
        if len(nama) > 20:
            print("panjang nama lebih dari 20")
            break
        nim = input()
        angkatan = input()
    
        baru.write("|" + " " + nama + " "*(22 - (len(nama)+1)) + "| " + nim + " | " + angkatan + " "*5 + "|" + "\n")
    baru.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+")
    
    print("Berhasil")
except:
    print("Gagal")
    
baru.close()