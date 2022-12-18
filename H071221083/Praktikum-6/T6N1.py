#soal rogram 1
# menyalin isi file .txt
a = input("File Asli : ")+'.txt'
b = input("File salinan : ")+'.txt'

#menghindari FileNotFoundError
try:
    def salin(a, b):
        with open(a) as asli:
            file_as = asli.read() #copy
            with open(b, "w") as salinan: 
                salinan.write(file_as) ; print("Berhasil")
    salin(a,b)

except FileNotFoundError: 
    print("Gagal")