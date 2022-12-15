nama_file = input("Masukkan nama file : ") + ".txt"
salinan   = input("Masukkan nama file salinan : ") + ".txt"

try :
    with open(nama_file, "r") as file:
        baca = file.read()
    with open(salinan, 'w') as copy:
        copy.write(baca)
    print('\nBerhasil')

except :
    print('\nGagal')