file = input("masukkan nama file: ")
file_salinan = input("masukkan nama file salinan: ")

try:
    with open(file + ".txt", "r") as file:
        data = file.read()
        file.closed

    with open(file_salinan + ".txt", "w") as file_salinan:
            if (data != -1):
                file_salinan.write(data)
                file_salinan.closed
    print("Berhasil")
except:
    print("Gagal")