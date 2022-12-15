file = input("masukkan nama file: ")
file_salinan = input("masukkan nama file salinan: ")

try:
    with open(file + ".txt", "r") as file:
        data = file.readlines()
        print(data)

        data[-1] = data[-1]+"\n"

        x = 0
        for i in data:
            if len(i) > x:
                x = len(i)

    with open(file_salinan + ".txt", "w") as file_salinan:
        for i in data:
            file_salinan.write(i.rjust(x))
            
    print("Berhasil")

except:
    print("Gagal")