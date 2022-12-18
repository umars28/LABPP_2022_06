#soal program 3
def all_string_rotation (x):
    banyak = len (x)
    for i in range (1,banyak+1):
        rotasi = list[banyak-i:] + list[:banyak-i]
        if banyak == 1:
            print (rotasi)
        else:
            print (rotasi,end='|')
list = input("Masukkan kata :")
all_string_rotation(list)