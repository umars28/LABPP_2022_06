#soal rogram 2
# menyalin isi file .txt rata kanan
a = input("File Asli : ")+'.txt'
b = input("File salinan : ")+'.txt'

#menghindari FileNotFoundError
try:
    with open(a) as asli:
        file_as = asli.readlines() ; n = []
        file_as[-1] += "\n"
        for x in file_as:
            n.append(len(x))
    with open(b, "w") as salinan:
        for i in file_as:
            salinan.write(i.rjust(max(n)))
    print("Berhasil")
except FileNotFoundError:
    print("Gagal")