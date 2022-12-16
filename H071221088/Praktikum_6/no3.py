filename = input() + ".txt"
n = int(input())

a = open(filename, "w")

try:
    a.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")
    a.write("|" + " Nama" + " "*17 + "|" + " NIM" + " "*8 + "|" + " Angkatan" + " " + "|" + "\n")
    a.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")

    for i in range(n):
        nama = input().replace(" ","_")
        if len(nama) > 20:
            print("nama tidak boleh lebih dari 20 karakter")
        nim = input()
        angkatan = input()
    
        a.write("|" + " " + nama + " "*(22 - (len(nama)+1)) + "| " + nim + " "*(11 - (len(nim)+1)) + " | " + angkatan + " "*5 + "|" + "\n")
    a.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+")
    
    print("Berhasil")
except:
    print("GAGAL")
    
a.close()