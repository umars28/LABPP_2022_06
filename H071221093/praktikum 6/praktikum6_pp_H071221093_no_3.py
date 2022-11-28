file = input()
jumlah = int(input())

nama = []
nim = []
angkatan = []

for i in range(jumlah): #perulangan untuk isi biodata sebanyak jumlah yang kita mau
    isi_nama = input('Masukkan Nama: ').replace(' ','_')
    if len(isi_nama) <= 20:
        nama.append(isi_nama)
    else:
        print('karakter pada nama melebihi batas (20 karakter)')
        exit()
    isi_nim = input('Masukkan NIM: ')
    nim.append(isi_nim)
    isi_angkatan = input('Masukkan Angkatan: ')
    angkatan.append(isi_angkatan)
    print('')

if len(isi_nama) <= 20:
    with open(f"{file}.txt","w") as f:
        nama_terpanjang = nama[0]
        #mencari nama yang terpanjang
        for CekNama in nama:
            if len(CekNama) > len(nama_terpanjang):
                nama_terpanjang = CekNama

         #baris pertama atau paling atas dari tabel
        f.write('+-'+('-'*len(nama_terpanjang))+'-+')
        f.write(('-'*12)+'+')
        f.write(('-'*10)+'+')

        #baris kedua untuk kolom format Nama, NIM, Angkatan
        f.write('\n| Nama'+(' '*(len(nama_terpanjang)-3))+'|') 
        f.write(' NIM'+(' '*(8))+'|')
        f.write(' Angkatan ' + '|')

        #baris ketiga batas antara format dan isi
        f.write('\n+-'+('-'*len(nama_terpanjang))+'-+')
        f.write(('-'*12)+'+')
        f.write(('-'*10)+'+')

        #baris selanjutnya isi sesuai banyak data yang di input
        for x in range(jumlah):
            f.write('\n| ')
            f.write(nama[x])
            f.write(' '*(len(nama_terpanjang)-len(nama[x]))+' | ')
            f.write(nim[x])
            f.write(' '*(11-len(nim[x]))+'| ')
            f.write(angkatan[x])
            f.write((' '*(9 - len(angkatan[x])))+'|')
        #baris paling akhir sebagai penutup
        f.write('\n+-'+('-'*len(nama_terpanjang))+'-+') 
        f.write(('-'*12)+'+')
        f.write(('-'*10)+'+')

        print('Berhasil')