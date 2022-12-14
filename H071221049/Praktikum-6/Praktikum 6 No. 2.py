nama_file = input("Masukkan nama file : ") + '.txt'
salinan   = input("Masukkan nama file salinan : ") + '.txt'
list_data = []
try : 
    with open (nama_file, 'r') as file:
        for i in file :
            i = i.replace ('\n','')
            list_data.append(i)

    with open (salinan, 'w') as copy:
        for j in range(len(list_data)):
            terpanjang = len(list_data[0])
            for k in list_data:
                if len(k) > terpanjang :
                    terpanjang = len(k)
            copy.write (' '*(terpanjang-len(list_data[j])) + f'{list_data[j]}\n')
        print('\nBerhasil')

except :
    print('\nGagal')
        