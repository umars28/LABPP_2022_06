#soal program 1
#make a function
def urutan(list_angka): 
    for x in range(len(list_angka)): #buat len untuk tau banyak karakter dalam list
        for y in range(x+1,len(list_angka)):
            if list_angka[x] > list_angka[y]:
                temp = list_angka[x]
                list_angka[x] = list_angka[y]
                list_angka[y] = temp
    return list_angka
print(urutan([7,4,-2,2,1,3,-2]))