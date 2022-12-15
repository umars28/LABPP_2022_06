try :
    namafile=input("masukkan nama file: ")
    jumlahdata=int(input("masukkan jumlah data: "))
    listnama=[]
    listnim=[]
    listangkatan=[]

    for x in range(jumlahdata) :
        nama=input("masukkan nama: ")
        listnama.append(nama)
        nim=input("masukkan nim: ")
        listnim.append(nim)
        angkatan=input("masukkan tahun angkatan: ")
        listangkatan.append(angkatan)

    longnama = listnama[0]
    for a in listnama :
        if len(a)>len(longnama) :
            longnama=a
    long=len(longnama)

    if long<=20:
        if len(nim)==10:
            if len(angkatan)==4:
                with open(f'{namafile}.txt','x') as file :
                    file.write('+'+'-'*(long+2)+'+')
                    file.write('-'*12+'+')
                    file.write('-'*10+'+\n')
                    file.write('|'+' Nama'+' '*(long-5+2)+'|')
                    file.write(' NIM'+' '*(10-4+2)+'|')
                    file.write(' Angkatan'+' '*(10-9)+'|\n')
                    file.write('+'+'-'*(long+2)+'+')
                    file.write('-'*12+'+')
                    file.write('-'*10+'+\n')

                    for j in range (jumlahdata) :
                        longnama = listnama[0]
                        for i in listnama :
                            if len(i)>long:
                                longnama=i
                        file.write(f'| {listnama[j]} '+' '*(long-len(listnama[j])))
                        file.write(f'| {listnim[j]}'+' '*1)
                        file.write(f'| {listangkatan[j]}'+' '*5+'|\n')

                    file.write('+'+'-'*(long+2)+'+')
                    file.write('-'*12+'+')
                    file.write('-'*10+'+\n')
                    print('Berhasil')
            else :
                print('Gagal')
        else :
            print('Panjang NIM maksimal 10 karakter')
    else :
        print('Nama terlalu panjang')
except :
    print('Gagal')